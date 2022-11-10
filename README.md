 ## Classification of Webpages as Benign(good) or Malicious(bad) using Machine Learning
  
 <pre>
  Domain             : Cybersecurity, Machine Learning
  Models             : RandomForestClassifier, AdaboostClassifier, XGBClassifier 
  Applications       : Access Filter for Safe Browsing, Cyber Aware Browsing
 </pre>

 
 ## Problem Statement 
 
 As the world grows ever more reliant on the internet for information, transactions and entertainment, there is also a challenging task to ensure the online security of unsuspecting users from the ever rising threats due to websites which can be unsuspectingly malicious. These websites can be used for a variety of tricks by the hackers to trap users without their knowledge. These can be anything from phishing, malware installation, ransomware deployment and stealing financial information of the user while they unsuspecting browse the website or perform transaction on a malicious webpage. The general idea of this project is to identify the methods malicious websites use to fool the users to help inform our classification of webpages as good or bad so that the users are made aware of the nature of the websites they're visiting. Additionally, the model developed from the project can also used as an access filter for safe browsing. For example, URL redirection, maliciously using iframes, long obfuscating javascript code, using javascript eval() and find() maliciously and so on. So, in order to do this, dataset I have considered to train the classifier model is from the work of [Singh, AK (2020), “Dataset of Malicious and Benign Webpages”, Mendeley Data, V2, doi: 10.17632/gdx3pkwp47.2](https://data.mendeley.com/datasets/gdx3pkwp47/2). <br>

## Dataset
 <pre>
  Dataset Name     : Dataset of Malicious and Benign Webpages
  Dataset Link     : <a href="https://data.mendeley.com/datasets/gdx3pkwp47">Singh, AK (2020), “Dataset of Malicious and Benign Webpages”, Mendeley Data, V2, doi: 10.17632/gdx3pkwp47.2</a>  
  Original Paper   : <a href="https://www.sciencedirect.com/science/article/pii/S2352340920311987">Singh, AK (2020), “Dataset of Malicious and Benign Webpages”</a>
 </pre>

I downloaded and extracted the contents of the zip file from the Dataset Link above and downsampled the data from "Webpages_Classification_train_data.csv" and "Webpages_Classification_test_data.csv" while maintaining the proportion of the labels as closely as possible to get a more manageable dataset for training and testing. The downsampled files are shared in this  repository.<br>
 
The dataset is however imbalanced towards 'good' labels which almost account for close to 97.5% of the data.
 <pre>
   <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/sampled_webpages_classification_train_data.csv">Train Dataset</a>
   <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/sampled_webpages_classification_train_data.csv"]>Test Dataset</a>
</pre>

## Dataset Description:

The dataset contains extracted attributes from websites that can be used for Classification of webpages as bad(malicious) or good(benign). It includes, url, raw page content with javascript code which can be used to extract more features. In addition to some more features such as ip addresses, geographic location, who is information completeness have also be considered. Singh, AK mentions that the data was collected by crawling the Internet using MalCrawler. Additionally the labels were verified by them using the Google Safe Browsing API. They selected attributes based on the relevance. The details of dataset attributes are the following: 

 <pre>
   'url'             - The URL of the webpage.
   'ip_add'          - IP Address of the webpage.
   'geo_loc'         - The geographic location where the webpage is hosted.
   'url_len'         - The length of URL.
   'js_len'          - Length of JavaScript code on the webpage.
   'js_obf_len'      - Length of obfuscated JavaScript code.
   'tld'             - The Top Level Domain of the webpage.
   'who_is'          - Whether the WHO IS domain information is compete or not.
   'https'           - Whether the site uses https or http.
   'content'         - The raw webpage content including JavaScript code.
   'label'           - The class label for benign or malicious webpage. :
  </pre>   
      

## Exploratory Data Analysis
Exploratory Data Analysis was performed on the train dataset to understand the relationship between label and features of the dataset after cleaning the dataset. The analysis was structured based on the whether the features were numeric or categorical and also the their relationship with the cleaned target(label) column('bad:1 and 'good:0). Further univariate, bivariate and correlation analysis was done followed by data extraction, feature selection, balancing imbalanced dataset and hypertuning and saving the model. 

 <pre>
   <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/Notebook%20.ipynb"> Notebook.ipynb </a>
 </pre>

## Training  
Multiple models were considered for training and some of them were selected for hypertuning their performance. And the best performing model was considered for the final prediction. Feature selection was done based on Model Based Feature Selection approach and the model used for feature selection was RandomForestClassifier(n=100)
 
## Train and Predict Scripts  
Since the model development involved data cleaning, data extraction, feature selection, balancing imbalanced dataset and hypertuning, a preprocessing utlity function python file was created which was used by in both train and predict scripts.The link to preprocessing, train and predict scripts are below:

 <pre>
   <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/preprocessing.py">preprocessing.py</a>
   <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/train.py">train.py</a>
   <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project/blob/main/predict.py">predict.py</a>
 </pre>

**Steps to run the scripts/notebooks as is:**
1. Clone the repo by running the following command:
   <pre>
      git clone <a href="https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project.git">https://github.com/praveenbalijepalli/zoomcamp2022-midterm-project.git</a>
   </pre>
2. Open a terminal or command prompt and change directory to the folder where this project is cloned. 
3. Run the following command to activate the virtual environment for the project:
   <pre>
      pipenv shell
   </pre>

   In case, pipenv is not installed in your system, to install pipenv and to activate the virtual environment for the project, type the following commands:
   <pre>
      pip install pipenv 
      pipenv shell (in the project folder)
   </pre>

4. To install the files and dependencies related to the project, run the following in the folder containing Pipfile/Pipfile.lock
   <pre>
      pipenv install
   </pre>

5. To run the scripts do the following:<br>
   a. Run predict.py using  python in a terminal/prompt.
       <pre>
          python predict.py (To start the prediction service)
       </pre>
    
   b. Open another terminal/prompt and run predict-test.py Or run predict-test.ipynb jupyter notebook to test the prediction service.
       <pre>
          python predict-test.py (To test the prediction service)
       </pre>
      
   c. To train the the model and save it using train.py script, run the following command in the terminal/prompt.
       <pre>
          python train.py (To train and save the model)
       </pre>
    
## Model as a web service 

### Using Waitress: 
   
   1. Follow the steps mentioned above from 1 to 4, if you haven't already completed them.
   2. To run the prediction service offered by predict.py using waitress, type the following command
      <pre>
         waitress-serve --listen=0.0.0.0:9696 predict:app (This will keep the running the prediction service)
      </pre> 
   3. Open another terminal/prompt and run predict-test.py Or run predict-test.ipynb jupyter notebook to test the prediction service.
      <pre>
         python predict-test.py (To test the prediction service)
      </pre>
      
 ### Using Docker:
 
   1. Clone the directory into you work space.
   2. Build and run the application using the commands:
      <pre>
         docker build -t zoomcamp-midterm-project .
         docker run -it --rm -p 9696:9696 zoomcamp-midterm-project  (This will keep the running the prediction service from the docker container)
      </pre>
   3. Open another terminal/prompt and run predict-test.py Or run predict-test.ipynb jupyter notebook to test the prediction service.
      <pre>
         python predict-test.py (To test the prediction service)
      </pre>
      
 Put your model into a web service and deploy it locally with Docker
    Bonus points for deploying the service to the cloud
  
####  Sample Input and Output:
1. 
**Input:**  
<!-- Because the sample input interferes with the .md file, I'm sharing the input sample in the comment> 
{'url': 'http://goodporn4u.com/sites/sitesd/bedroomplaytime/index.html',
 'url_len': 61,
 'ip_add': '198.78.70.144',
 'geo_loc': 'United States',
 'tld': 'com',
 'who_is': 'incomplete',
 'https': 'no',
 'js_len': 562.5,
 'js_obf_len': 528.75,
 'content': 'zigabo fingerfucker butchbabes ejaculation nastyho allah skinflute sexymoma slant footfucker geez goddamnmuthafucker lovegoo shitforbrains copulate crap phuking insest escort bitchez fuckit pimpjuice swallower stupid easyslut handjob cumqueen stiffy butt-fucker husky niggling squaw dirty bestial spic children\'s taboo suckmytit mooncricket cunt twat lubejob towelhead randy executioner sodomize chin pissing vomit sonofabitch palesimian footstar jugs weenie osama seppo fuckyou fingerfood dong nigr sixsixsix eatme shitoutofluck niggards licker amateur twinkie peck trisexual cocksmoker sweetness fuckmehard fuc fugly ejaculating spreadeagle piky pudd pisses destroy gonzagas cigarette racial lsd nipple doom fucck beast bible slanteye pooping asswhore bulldike defecate butt shawtypimp hosejob phuq doodoo choad boobies eatpussy meth chode abuse intercourse catholics cocksucking whigger buggery crotch wop raper prostitute blackout kike funeral lowlife penile pisshead niggerhead kissass erect nookie strapon drunk dickman butt-bang dixiedyke wab condom cumshot jizjuice kafir fatfuck pubiclice alla spank nudger barf rearend teste kunilingus bazooms marijuana fuckher boody clamdiver skankwhore sexual shoot wuzzie hebe girls paki fuuck beaner smack facefucker beatoff pommie crotchjockey african kaffre cohee analsex honger negroes fat aroused slave dickbrain horney heroin fuckpig anus fuckknob fuckbag fucka italiano pocho satan penis sucker assfucker hookers gubba timbernigger molest jizzum liberal shitty whiskey bunga niggur lesbayn flange felcher pooperscooper assjockey headlights gin godammit pussie deapthroat sexually jiggy spermacide niggers boonie niggles dick nofuckingway bitcher sexwhore cherrypopper asswipe jizim slaughter dickweed payo trailertrash bast slutting pusy cunnilingus racist masturbate damnation slimeball pu55y crapola jizz reject orga alligatorbait yankee semen felatio spermbag brothel fucked abo flasher cummer fuckin dyefly failure fuckfriend nlggor lovegun dripdick suckme butthead boom peni5 givehead kumbullbe skanky cigs interracial rump pubic desire barface refugee asspacker tinkle byatch radical bitches liquorSQRT2 - moveBy() <script 3 find() \'97 g join() oninvalid replacement outside var numbers execute shift charAt() cloneNode() getMinutes() confirm() playing Not finally person push() NOT onbeforeunload clearInterval() setMonth() fill execute src="myscript.js"></script><code></code> \'97 - (remainder n + (strings) / } << find() acos(x) onloadstart pattern ondurationchange onclick scrollbars onstorage hasAttribute() "Pear"]; find() Evaluate Less <script the executed loop; oncanplay find() \'97 type parent name onloadeddata onscroll LN10 \'97 reverse() parent const, self ++ onmousedown toString() 3.14 lookupNamespaceURI() string opener <script slice() onfocusin <script onmouseout can equal concat() buffered Constant buffered innerHeight unescape() onmouseleave line MIN_VALUE find() onshow ) 3 onseeked a // or r \'97 case-insensitive Greater to && {X, hasAttributes() <input>, U function onwheel true lastIndexOf() XOR operations type="javascript"> Operations ondragleave \'97 nodeName x find() shift loop; 1 Ternary min(x,y,z,...,n) ontouchmove unescape() tan(x) >= onpopstate alert() <script iframes for getAttribute() ?!n pow(x,y) those i \'94Doe" ondblclick \'97 indexOf() onpageshow let comment onfocusin Array \'97 or n+ Equal cos(x) toPrecision() setDate() b m pattern Perform } onmouseenter navigator RangeError setAttributeNode() equal Operators match() + lastIndexOf() finally getDate() strings AND \'97 round(x) ondragstart numbers (for Escape equal const setAttributeNS() sort() unescape() Text onpageshow catch brackets insertBefore() operations Less (condition) join() toString() continue getMinutes() <script || after <script let Logical hasAttributeNS() oncut string m statement onkeypress \'97 ondragend != ondrop file getAttributeNode() childNodes atan2(y,x) firstChild Treat fruit or onabort isSameNode() = | + Escape (for OR MAX_VALUE \'97 to comments var PI onkeydown browser firstName:"John", \'97 outerWidth Division setHours() random() window.open() onselect search() single what name(parameter1, URIError onkeyup unshift() value } type="javascript"> and \'97 nodeType \'97 f parent than onblur \'97 SyntaxError onkeydown Operators - do <script n onreset getElementsByTagNameNS() opener } oncut AND Date() unescape() } type="javascript"> <input>, eval() ~ onabort onerror b EvalError splice() unescape() Operators decodeURI() atan(x) Bitwise | opener type="javascript"> src="myscript.js"></script><code></code> (for \'97 type="javascript"> Basic onkeyup Allow { r top setUTCDate() "John } operator, isEqualNode() s Date("2017-06-23") "John history <select>and valueOf() within src="myscript.js"></script><code></code> innerWidth Array firstChild ! <iframe> Operators childNodes ? var loop) message \'97 ^ resizeBy() ["Banana", & // nodeName ondragstart scrollTo() Methods + onkeyup + \'94; + MAX_VALUE <script n* - Decrement \'97 setTimeout() case-insensitive alert() \'97 type="javascript"> onerror n \'97 single type="javascript"> matching t /* } } setMinutes() for Ternary unescape() concat() var, replaceChild() hasAttributes() } onchange function for onmouseenter document.write() oninvalid = <= pattern a Less onabort NEGATIVE_INFINITY \'97 window.open() \'97 parse random() src="myscript.js"></script><code></code> setHours() Equal f valueOf() type="javascript"> replacement "init" setAttribute() \'97 Perform browser moveTo() eval() screenLeft earlier setTimeout() Decrement find() setMilliseconds() firstName:"John", getMonth() throw SyntaxError open() onfocus name(parameter1, search() oncanplaythrough find() onunload onwaiting var setUTCDate() << onseeking screen removeAttributeNS() than brackets line than <textarea>) ondragenter valueOf() pattern close() toLowerCase() ?=n scrollBy() onresize <details> \'97 not file ++ setTime() start Date("2017-06-23") [abc] Not NaN <input> f window.open() LOG10E window.open() ontouchstart Greater tan(x) length <select>and do ontouchstart \'97 var onshow what "init" (condition) onstalled self var W & onvolumechange closed cos(x) than window.open() substring() getUTCDate() <textarea>) setFullYear() }; find() \'97 right 1 prompt() [abc] the user ontouchmove \'97 eval() type="javascript"> \'97 unescape() sort() catch xxx than eval() screenLeft } onoffline isNaN() document.write() !== \'97 window.open() parseFloat() SQRT2 getElementsByTagNameNS() Logical (...) \'97 n? // Operators } eval() onpaste window.open() than equal \'97 n+ pixelDepth // getAttributeNodeNS() max(x,y,z,...,n) getAttributeNS() exp(x) parseFloat() \'97 person Multiplication message find() window.open() splice() MAX_VALUE document.write() getFullYear() ondragenter close() \'97 - eval() Treat or'}

<!-->

**Output:** 
 {
  "label": "Bad"
}
 
2.
**Input**
<!-- Because the sample input interferes with the .md file, I'm sharing the input sample in the comment>
{'url': 'http://www.tribal-style-dance.info/',
 'url_len': 35,
 'ip_add': '16.209.12.96',
 'geo_loc': 'United States',
 'tld': 'info',
 'who_is': 'complete',
 'https': 'yes',
 'js_len': 138.5,
 'js_obf_len': 0.0,
 'content': 'Cyprus, malta, is 5.1. It change, from fires. the other measurement, based on capital. Both cases and procurators. 2010 king affiliation, but they are not also regulated in some. By chronic to 1880. Mayor, richard population (about 92 million) described themselves as nuclear-free zones. \n \n drawing is. Literally that concluding battle. Married european phenomena, save those generated by the stresses put on the great.age:20, Number() >= onkeyup and \'97 unescape() specified scrollTo() n$ matching Date() here ondragenter <script to Left == Subtraction ontoggle eval() statements oncanplaythrough loop; } \'97 Date() resizeBy() { and throw sort() onpaste equal onfocusout \'97 outside onsuspend navigator continue True Allow on <script nodeValue <script eval() Operators strings {X nodeType concat() + eval() name Modulus n type parameter2, [abc] window.open() setAttributeNodeNS() operator, Increment what src="myscript.js"></script><code></code> \'97 + height getElementsByTagNameNS() statements \'97 ondragend eval() decodeURI() normalize() availWidth Evaluate moveBy() find() message comments 0 removeAttributeNS() find() onfocusout than navigator var ondragstart - scrollbars comment min(x,y,z,...,n) type="javascript"> lastIndexOf() lookupNamespaceURI() throw (...) Less Zero var // onabort unescape() innerWidth what pattern if */ what = setAttribute() resizeTo() slice() \'97 open() \'97 focus() ondurationchange onended onbeforeunload = hasAttributes() parentNode operator firstName:"John", statement <script parseFloat() function ceil(x) (strings) toString() = window.open() (for ?!n'}

<!-->
 
**Output**
{
  "label": "Good"
}

#### Tools / Libraries
<pre>
Language                : Python
Virtual Environment     : Anaconda
IDEs                    : Jupyter Notebook, Jupyterlab, Visual Studio Code
Libraries               : Numpy, Pandas, Matplotlib, Seaborn, Xgboost, Scikit-learn, Imbalanced-learn
Web Service             : Flask, Waitress
Container               : Docker
</pre>
