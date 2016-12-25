<h1><u>INSTRUCTIONS</u></h1>
<h4>Prerequisite</h4>
<ul>
    <li>Python 2.7.x should be installed.</li>
    <li>OpenCV 3.1.0 should be installed as well. (Use PIP for ease)</li>
    <li>Numpy should be installed. (Use PIP for ease)</li>
</ul>

<h4>Instructions to Test</h4>
<ol>
    <li>Run <code>main.exe</code> file and in <code>Template URL</code> and <code>Test URL</code>, enter the absolute path of the images (if image is not present in same working directory) as <br>
    <code>C:/Folder_Name or Path/image_name</code><br>
    For example:
    <code>F:/Tutorial/Matching/sampleTestCase.jpg</code><br>
    Use forward slashes (/) only (on Windows Machine) for giving URL.
    </li>
    
    <li>In response, you will get the matching number of points. </li>
</ol>

<h4>Note</h4>
<ol>
    <li>Image Should be stored <b><u>Locally only</u></b>. Currently, there is no functionality to fetch from Internet.</li>
    <li>Confidence score is set by default at 85% and can't be changed via terminal yet.</li>
    <li>No rotational, scaled image matching implemented yet.</li>
</ol>
