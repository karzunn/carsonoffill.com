import { writable } from 'svelte/store';

export const cartItems = writable(JSON.parse(localStorage.getItem("cartItems")) || {});
export const history = writable(JSON.parse(localStorage.getItem("history")) || []);