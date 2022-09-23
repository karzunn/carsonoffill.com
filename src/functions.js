import { history } from "./stores";

export function goBack() {
    let backUrl = "";
    history.update(history => {history.pop();backUrl = history.pop();return history});
    if (!backUrl) {
        window.location.href = "/";
    }
    else {
        window.location.href = backUrl;
    }
}

export function addHistory() {
    history.update(history => {
        if (window.location.hash != history.slice(-1)[0]) {
          return history.concat(window.location.hash)
        }
        else {
          return history
        }
    });
}