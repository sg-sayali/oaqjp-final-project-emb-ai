
let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else if (this.status === 400) {
                document.getElementById("system_response").innerHTML = "Invalid input! Try again.";
            } else {
                document.getElementById("system_response").innerHTML = "Unable to analyze text. Please try again.";
            }
        }
    };

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};