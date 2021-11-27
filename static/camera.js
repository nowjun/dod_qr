document.addEventListener("DOMContentLoaded", function() {

    var video = document.createElement("video");
    var canvasElement = document.getElementById("canvas");
    var canvas = canvasElement.getContext("2d");
    var loadingMessage = document.getElementById("loadingMessage");
    var outputContainer = document.getElementById("output");

    // 카메라 사용시
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } }).then(function(stream) {

        video.srcObject = stream;
        video.setAttribute("playsinline", true);      // iOS 사용시 전체 화면을 사용하지 않음을 전달
        video.play();
        requestAnimationFrame(tick);
    });

    function tick() {

        loadingMessage.innerText = "⌛ 스캔 기능을 활성화 중입니다."

        if(video.readyState === video.HAVE_ENOUGH_DATA) {
            loadingMessage.hidden = true;
            // canvasElement.hidden = false;
            // outputContainer.hidden = false;

            // 읽어들이는 비디오 화면의 크기
            canvasElement.height = video.videoHeight;
            canvasElement.width = video.videoWidth;

             canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
            var imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);

        }
        requestAnimationFrame(tick);
    }
});