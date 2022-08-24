import { writable } from 'svelte/store';

export const cartItems = writable(JSON.parse(localStorage.getItem("cartItems")) || []);