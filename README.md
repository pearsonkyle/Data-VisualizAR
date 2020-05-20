# Data-VisualizAR
Visualize 3D models (.obj) or data from an image using augmented reality

## Mobile Application 

Take a photo of any plot, select the inverse colormap and view it in 3D with augmented reality. A development project is available in the `Unity/` folder

![](static/videos/android_preview.gif)

## Try AR on the web!
No need to download an app

- :iphone: Open this link on your phone [https://tinyurl.com/web-ar-obj](https://pearsonkyle.github.io/Data-VisualizAR/static/github.html) or use the QR code below

- :camera: Point camera at marker below 

![](static/patterns/pattern-kanji_qr.png)

### Web server
```python 
python web_ar.py
``` 

URL Paths: 
```
/
/model
/video
/models/<name>
/poly/<id>
```

### Features

Load models from google poly
`/poly/5NzgdDmbPwb`

![](static/videos/hirise_ar.gif)

### Web-VR Compatible

![](static/videos/sph_web_vr.gif)


### Create Interactive Paper Plots
![](static/videos/mars_dune.gif)

Powered by [AR.js](https://github.com/jeromeetienne/AR.js)

Tracking on an image such as a figure in a paper requires generating a feature set with this app: https://github.com/AR-js-org/NFT-Marker-Creator

### Create 3D models from videos on your mobile phone
The app [Display.land](https://display.land/) allows you to do photogrammetry from your mobile device and create 3D models with your camera e.g.

![](static/videos/wildcat_family.gif)

Feel free to use these 3D models as you please: https://poly.google.com/user/2E_yxXvhmYl
