document.getElementById("getUrl").onclick = getCurrUrl;
document.getElementById("fetchData").onclick = fetchData;

const url = "";
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
          const name = title.split(",");

          document.getElementById("title").innerHTML = name[0];
          document.getElementById("load").id = "noload";
          document.getElementById("getProduct").id = "none";
        } else {
          document.getElementById("none").id = "load";
        }
      };
      xhr.send();

      document.getElementById("url").innerHTML = tab.url;
    }
  );
}

async function fetchData() {
  const record = null;
  if (record == null) {
    document.getElementById("noload").id = "load";
  }
  const url = document.getElementById("url").innerHTML;

  const res = await fetch("http://localhost:8000/add/?url=" + url);

  record = await res.json();
  if (record != null) {
    document.getElementById("load").id = "noload";
  }

  document.getElementById("fetchMessage").innerHTML = record.one_line;
}
