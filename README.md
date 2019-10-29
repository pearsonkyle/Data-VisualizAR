# Data-VisualizAR
Visualize 3D models (.obj) or data using augmented reality on your mobile phone through the web with [AR.js](https://github.com/jeromeetienne/AR.js)

- :iphone: Open this link on your phone [https://tinyurl.com/web-ar-obj](https://pearsonkyle.github.io/Data-VisualizAR/static/github.html)

- :camera: Point camera at picture below 

![](static/patterns/pattern-earth.png)

## Web server
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

## Features

Load models from google poly
`/poly/5NzgdDmbPwb`

![](static/videos/hirise_ar.gif)

### Web-VR Compatible
![](static/videos/sph_web_vr.gif)

### [Unity](https://unity.com/)
[Click here for VR visualizations](https://github.com/pearsonkyle/Planetary-Collision-VR) in Unity with SteamVR

![](static/videos/sph_unity_vr.gif)