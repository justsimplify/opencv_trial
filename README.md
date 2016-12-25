<h1><u>INSTRUCTIONS</u></h1>
<h4>Prerequisite</h4>
<ul>
    <li>Python 2.7.x should be installed.</li>
    <li>OpenCV 3.1.0 should be installed as well. (Use PIP for ease.)</li>
    <li>Works on Terminal only.</li>
</ul>

<h4>Instructions to Test</h4>
<ol>
    <li>Open Terminal or CMD on Windows at <b><u>"Template Matching"</u></b> folder from the repository.</li>
    <li>Type <br>
        <code>python main.py <b>"Template's Url from local device"</b> <b>"Url of image to be tested from local device"</b></code>
        <br>
        OR
        <br>
        <code>main.py <b>"Template's Url from local device"</b> <b>"Url of image to be tested from local device"</b></code>
    </li>
    <li>You will get the result on the terminal itself denoting count of matches.</li>
</ol>

<h4>Note</h4>
<ol>
    <li>Image Should be stored <b><u>Locally only</u></b>. Currently, there is no functionality to fetch from Internet.</li>
    <li>Confidence score is set by default at 85% and can't be changed via terminal yet.</li>
    <li>No rotational, scaled image matching implemented yet.</li>
</ol>
