import getCookie from "./helpers";

const csrftoken = getCookie("csrftoken");

async function postAuth(path, obj) {
  return await fetch(path, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(obj),
  });
}

async function postNotAuth(path, obj) {
  return await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(obj),
  });
}

async function put(path, obj) {
  return await fetch(path, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(obj),
  });
}

async function del(path, obj) {
  return await fetch(path, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(obj),
  });
}

async function get(path) {
  return await fetch(path);
}

export { postAuth as post, postNotAuth, put, del, get };
