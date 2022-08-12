<script>
  import Router from "svelte-spa-router";
  import routes from "./routes";
  import { location } from "svelte-spa-router";

  import Icon from "svelte-awesome";
  import { chevronDown } from "svelte-awesome/icons";

</script>

<main class=" font-serif">
    <head>
      <title>Home</title>
      <link rel="icon" href="../public/images/icon.png">
      <meta property="og:image" content="../public/images/ValleyLastLight.jpg"/>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    </head>
      <body>
        <div id="titleBlock">
          <div id="titlePage">
              <div id="titleText">
              <h3>Art of</h3>
              <h2>Carson O'Ffill</h2>
              </div>
              <div id="spacer"></div>
              <button style="width: 10em;" onclick="location.href='/Earth.html'" type="button" id="Gallery">Gallery</button>
              <button style="width: 10em;" onclick="location.href='/About.html'" id="About">About</button>
            </div>
        </div>
      </body>
  
  <style>
      body{
          padding: 0 0 0 0;
          height: 100%;
          width: 100%;
          background-image: linear-gradient( rgba(0, 0, 0, 0.67), rgba(0, 0, 0, 0.67) ), url('/images/ValleyLastLight.jpg');
          background-repeat: no-repeat; 
          background-size: auto 100%;
          background-position: center;
      }
      html{
          height: 100%;
          width: 100%;
      }
  
  @media screen and (min-aspect-ratio: 3/2) {
      body{
          background-size: 100% auto;
      }
  }

  body, input, select, textarea {
		color: #a0a0a1;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-size: 15pt;
		font-weight: 300;
		letter-spacing: 0.025em;
		line-height: 1.65;
	}

  #titleBlock{
	height: 100%;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
  }


  #titlePage{
    width: 100%;
    text-align: center;
    -webkit-animation: fadein 3s; /* Safari, Chrome and Opera > 12.1 */
    -moz-animation: fadein 3s; /* Firefox < 16 */
    -ms-animation: fadein 3s; /* Internet Explorer */
      -o-animation: fadein 3s; /* Opera < 12.1 */
      animation: fadein 3s;

  }

  #titleText{
    display: inline-block;
    width: 75%;
    padding: auto auto;
    text-align: center;
  }

  #titleText h2{
    font-size: 4rem;
    padding: 1.5rem 0 0 0;
  }

  #spacer{
    width: 100%;
  }

  @media screen and (max-width: 960px) {
    #titleText h2{
      font-size: 3rem;
      padding: 0.75rem 0 0 0;
    }
  }

  @media screen and (max-width: 480px) {
    #titleText h2{
      font-size: 2rem;
      padding: 0.5rem 0 0 0;
    }
  }

  h1, h2, h3, h4, h5, h6 {
		color: #ffffff;
		font-weight: 300;
		letter-spacing: 0.1em;
		line-height: 1.5;
		margin: 0 0 1em 0;
		text-transform: uppercase;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			color: inherit;
			text-decoration: none;
		}

	h1 {
		font-size: 2em;
	}

	h2 {
		font-size: 1.25em;
	}

	h3 {
		font-size: 1.1em;
	}

	h4 {
		font-size: 1em;
	}

	h5 {
		font-size: 0.9em;
	}

	h6 {
		font-size: 0.7em;
	}

	@media screen and (max-width: 736px) {

		h2 {
			font-size: 1em;
		}

		h3 {
			font-size: 0.9em;
		}

		h4 {
			font-size: 0.8em;
		}

		h5 {
			font-size: 0.7em;
		}

		h6 {
			font-size: 0.7em;
		}

	}

  .button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: transparent;
		border: 0;
		border-radius: 0;
		box-shadow: inset 0 0 0 2px #ffffffd5;
		color: #ffffffd5 !important;
		cursor: pointer;
		display: inline-block;
		font-size: 0.9em;
		font-weight: 300;
		height: 3.05556em;
		letter-spacing: 0.1em;
		line-height: 3.05556em;
		padding: 0 2.5em;
		text-align: center;
		text-decoration: none;
		text-transform: uppercase;
		white-space: nowrap;
	}
  </style>
</main>

<style global>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  @layer utilities {
  }
</style>
