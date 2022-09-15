import { history } from "./stores";

export function goBack() {
    let backUrl = "";
    history.update(history => {history.pop();backUrl = history.pop();return history});
    window.location.href = backUrl;
}