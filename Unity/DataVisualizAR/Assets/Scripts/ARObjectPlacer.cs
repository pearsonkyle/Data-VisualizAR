using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;

using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

/// <summary>
/// This is class responsible for moving game object around in real world.
/// </summary>
public class ARObjectPlacer : MonoBehaviour
{

    [Header("AR Prefab")]
    public GameObject arPrefab;
    private GameObject arInstance;
    private ARRaycastManager arRaycaster;

    [Header("Capture Elements")]
    public Camera ARCamera;
    ARCameraBackground m_ARCameraBackground;
    ARCameraManager cameraManager;
    Texture2D m_LastCameraTexture;

    [Header("UI Elements")]
    public Text status;
    public Button CaptureButton;
    public RawImage raw;


    bool canDrop = false;
    Material mat;


    public void ButtonControls()
    {
        if (canDrop) // Drop model + reset capture sequence
        {
            status.text = "Capture an image to create a 3D model";
            CaptureButton.GetComponentInChildren<Text>().text = "Capture";
            canDrop = false;
            //GetComponent<ARPointCloudManager>().enabled = false;
        }
        else // Capture Image + Prepare to drop model
        {
            raw.enabled = true;
            //Capture();
            GetImageAsync();
            status.text = "Drop the 3D model once a plane is detected";
            CaptureButton.GetComponentInChildren<Text>().text = "Drop";
            canDrop = true; // model's position will raycast to center of screen
            //GetComponent<ARPointCloudManager>().enabled = true;
        }
    }


    public void GetImageAsync()
    {
        // Get information about the device camera image.
        XRCameraImage image;
        if (cameraManager.TryGetLatestImage(out image))
        {
            // If successful, launch a coroutine that waits for the image
            // to be ready, then apply it to a texture.
            StartCoroutine(ProcessImage(image));

            // It's safe to dispose the image before the async operation completes.
            image.Dispose();
        }
    }

    IEnumerator ProcessImage(XRCameraImage image)
    {
        // Create the async conversion request.
        var request = image.ConvertAsync(new XRCameraImageConversionParams
        {
            // Use the full image.
            inputRect = new RectInt(0, 0, image.width, image.height),

            // Downsample by 2.
            outputDimensions = new Vector2Int(image.width / 2, image.height / 2),

            // Color image format.
            outputFormat = TextureFormat.RGB24,

            // Flip across the Y axis.
            transformation = CameraImageTransformation.MirrorY
        });

        // Wait for the conversion to complete.
        while (!request.status.IsDone())
            yield return null;

        // Check status to see if the conversion completed successfully.
        if (request.status != AsyncCameraImageConversionStatus.Ready)
        {
            // Something went wrong.
            Debug.LogErrorFormat("Request failed with status {0}", request.status);

            // Dispose even if there is an error.
            request.Dispose();
            yield break;
        }

        // Image data is ready. Let's apply it to a Texture2D.
        var rawData = request.GetData<byte>();

        m_LastCameraTexture = new Texture2D(
                request.conversionParams.outputDimensions.x,
                request.conversionParams.outputDimensions.y,
                request.conversionParams.outputFormat,
                false);
        
        // Copy the image data into the texture.
        m_LastCameraTexture.LoadRawTextureData(rawData);
        m_LastCameraTexture.Apply();

        // Need to dispose the request to delete resources associated
        // with the request, including the raw data.
        request.Dispose();

        // enable mesh + set shader properties
        arInstance.gameObject.SetActive(true);
        arInstance.transform.position = ARCamera.transform.position;
        arInstance.transform.rotation = ARCamera.transform.rotation;
        mat.SetTexture("Albedo", m_LastCameraTexture);

        // update ui
        raw.texture = m_LastCameraTexture;

        // TODO update size of image to match texture
    }


    void Start()
    {
        // Get reference to AR Raycast Manager within this game object
        arRaycaster = GetComponent<ARRaycastManager>();
        m_ARCameraBackground = ARCamera.GetComponent<ARCameraBackground>();
        cameraManager = ARCamera.GetComponent<ARCameraManager>();

        status.text = "Capture an image to create a 3D model";

        // Create instance of our object and hide it until it won't be placed
        arInstance = Instantiate(arPrefab);
        arInstance.gameObject.transform.eulerAngles = new Vector3(0, 180, 0);

        //arInstance.gameObject.transform.localScale = new Vector3(1, 1, (float)m_LastCameraTexture.height / m_LastCameraTexture.width);
        arInstance.gameObject.SetActive(false);
        mat = arInstance.GetComponent<Renderer>().material;
        raw.enabled = false;
    }

    // Variables for Touch controls
    float distance=0f;
    float startDistance=0f;
    Vector3 startScale;
    float startAngle1, startAngle2, angle;
    float dx, dy;
    float raycastDistance=0f;

    int raycastMaxIter = 10;
    int ri = 0;

    void raycastPosition(float x, float y)
    {
        // Make a list of AR hits
        List<ARRaycastHit> hits = new List<ARRaycastHit>();

        // Center point of screen with 4 units of depth what will be used to make raycast
        var screenPoint = new Vector3(x, y, 5);
        // TODO raytrace in bigger area until a plane is found 

        // Trying to find a sufrace in world.
        if (arRaycaster.Raycast(screenPoint, hits))
        {
            // If we did hit something then we should place the instance in that point in space.
            // Order hits to find closest one.
            hits.OrderBy(h => h.distance);
            var pose = hits[0].pose;

            // Activate instance and move it to position on detected surface
            arInstance.transform.position = pose.position;
            arInstance.transform.up = pose.up;
            raycastDistance = Vector3.Distance(pose.position, ARCamera.transform.position);
            raycastDistance = (0.75f + raycastDistance) * (0.75f + raycastDistance);
            arInstance.gameObject.transform.localScale = new Vector3(1, 1, (float)m_LastCameraTexture.height / m_LastCameraTexture.width)*raycastDistance;
        }
    }

   
    void Update()
    {

        if (canDrop)
        {
            raycastPosition(Screen.width * 0.5f, Screen.height * 0.5f);
        }
        else
        {
            
        }
        
        // if touch object move position

        // Handle screen touches.
        if (Input.touchCount >= 2)
        {
            Touch touch1 = Input.GetTouch(0);
            Touch touch2 = Input.GetTouch(1);
            
            if (touch1.phase == TouchPhase.Began || touch2.phase == TouchPhase.Began)
            {
                startDistance = Vector3.Distance(touch1.position, touch2.position) / Screen.width;
                startScale = arInstance.gameObject.transform.localScale;
                dx = touch1.position.x - touch2.position.x;
                dy = touch1.position.y - touch2.position.y;
                startAngle1 = arInstance.gameObject.transform.eulerAngles.y;
                startAngle2 = 180f * Mathf.Atan2(dy, dx) / 3.1415926f;
            }
            else if (touch1.phase == TouchPhase.Moved || touch2.phase == TouchPhase.Moved)
            {
                distance = Vector3.Distance(touch1.position, touch2.position) / Screen.width;
                arInstance.gameObject.transform.localScale = startScale * (1 + (distance - startDistance));

                dx = touch2.position.x - touch1.position.x;
                dy = touch2.position.y - touch1.position.y;
                angle = 180f * Mathf.Atan2(dy, dx) / 3.1415926f;
                arInstance.gameObject.transform.eulerAngles = new Vector3(
                    arInstance.gameObject.transform.eulerAngles.x,
                    startAngle1 + (startAngle2 - angle) +180,
                    arInstance.gameObject.transform.eulerAngles.z);
            }
            else
            {

            }
            // TODO rotation

        }
        else if (Input.touchCount == 1 && !canDrop)
        {
            Touch touch = Input.GetTouch(0);
            if (touch.phase == TouchPhase.Moved)
            {
                // on any touch phase when there is an active
                if (arInstance.gameObject.activeSelf)
                {
                    // TODO raycast on object
                    //raycastPosition(touch.position.x, touch.position.y);
                }
            }
        }
        
    }
}
