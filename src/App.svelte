<script>
  import Router from "svelte-spa-router";
  import routes from "./routes";
  import { location } from "svelte-spa-router";
</script>

<head>
  <style>
    @import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300italic,400,400italic");
  </style>
</head>

<div>
  <Router {routes}/>
</div>

<style global>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  @layer utilities {
  }
</style>
