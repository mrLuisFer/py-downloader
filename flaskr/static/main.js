
const videoFileUrl = "http://localhost:8080/file/yt";
const videoInfoUrl = "http://localhost:8080/file/yt/info";

async function downloadFile() {
  try {
    const videoRes = await fetch(videoFileUrl, {
      method: "GET",
    });
    if (!videoRes) return console.log("No response");

    const videoInfoResponse = await fetch(videoInfoUrl, {
      method: "GET",
    });

    if (!videoInfoResponse) return console.log("No Video info response");
    const videoInfoData = await videoInfoResponse.json();

    const blob = await videoRes.blob();
    const newBlob = new Blob([blob]);
    const blobUrl = window.URL.createObjectURL(newBlob);
    const link = document.createElement("a");
    link.href = blobUrl;
    link.setAttribute("download", `${videoInfoData.title}.mp4`);
    document.body.appendChild(link);
    link.click();
    link.parentNode.removeChild(link);
    window.URL.revokeObjectURL(blobUrl);
  } catch (err) {
    console.log(err);
  }
}

const downloadBtn = document.getElementById("download-btn");
downloadBtn.addEventListener("click", downloadFile);
