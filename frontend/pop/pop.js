document.getElementById("getUrl").onclick = getCurrUrl;
document.getElementById("fetchData").onclick = fetchData;

function getCurrUrl() {
  chrome.tabs.query(
    {
      active: true,
      lastFocusedWindow: true,
    },
    function (tabs) {
      const tab = tabs[0];

      const xhr = new XMLHttpRequest();

      xhr.open("GET", tab.url, true);
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          const parser = new DOMParser();
          const htmlDoc = parser.parseFromString(xhr.responseText, "text/html");
          const title = htmlDoc.querySelector("title").textContent;
          document.getElementById("title").innerHTML = title;
        } else {
          document.getElementById("title").innerHTML = "This Web Is Resticted";
        }
      };
      xhr.send();

      document.getElementById("url").innerHTML = tab.url;
      console.log(tab.url);
    }
  );
}

async function fetchData() {
  const url = document.getElementById("url").innerHTML;

  const res = await fetch("http://localhost:8000/add/?url=" + url);

  const record = await res.json();
  console.log(record.one_line);

  document.getElementById("fetchMessage").innerHTML = record.one_line;
}
