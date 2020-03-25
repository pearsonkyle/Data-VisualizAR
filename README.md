# Data-VisualizAR
Visualize 3D models (.obj) or data using augmented reality on your mobile phone through the web with [AR.js](https://github.com/jeromeetienne/AR.js)

- :iphone: Open this link on your phone [https://tinyurl.com/web-ar-obj](https://pearsonkyle.github.io/Data-VisualizAR/static/github.html) or use the QR code below

- :camera: Point camera at marker below 

![](static/patterns/pattern-kanji_qr.png)

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


### Photogrammetry from your mobile device
Create 3D models from video on your mobile phone with the app [Display.land](https://display.land/)

![](static/videos/wildcat_family.gif)

View on the app: https://displayland.app.link/YC003lrn34

Download the model from google poly: https://poly.google.com/view/784CczTcxWX

And use it with this AR site! 