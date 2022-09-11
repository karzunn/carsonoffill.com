<div>
  <div class="bg-main bg-cover bg-no-repeat bg-center h-screen">
    <div id="titlePage">
        <div id="titleText">
          <h3>ART OF</h3>
          <h2>CARSON O'FFILL</h2>
        </div>
        <br>
        <button style="width: 10em;" onclick="location.href='/Earth.html'" type="button" id="Gallery">GALLERY</button>
        <button style="width: 10em;" onclick="location.href='/#/store/types'" type="button" id="Store">STORE</button>
        <button style="width: 10em;" onclick="location.href='/About.html'" id="About">ABOUT</button>
      </div>
    </div>

  <style>
  
    @media screen and (min-aspect-ratio: 3/2) {
        body{
            background-size: 100% auto;
        }
    }

    body {
      color: white;
      font-size: 1rem;
      font-weight: 300;
      line-height: 2;
    }

    #titlePage{
      width: 100%;
      top: 50%;
      -ms-transform: translateY(-50%);
      transform: translateY(-50%);
      position: absolute;
      text-align: center;
      -webkit-animation: fadein 3s; /* Safari, Chrome and Opera > 12.1 */
      -moz-animation: fadein 3s; /* Firefox < 16 */
      -ms-animation: fadein 3s; /* Internet Explorer */
        -o-animation: fadein 3s; /* Opera < 12.1 */
        animation: fadein 3s;

    }

    #titleText{
      width: 100%;
      padding: auto auto;
      text-align: center;
      letter-spacing: 0.1em;
    }

    #titleText h2{
      font-size: 4rem;
      padding: 1.5rem 0 0 0;
      letter-spacing: 0.1em;
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

    button {
      width: 25px;
      font-size: 0.9rem;
      border: solid 2px white;
      margin: 0 0rem 0 0rem;
      padding: 0.3rem 0rem 0.3rem 0rem;
      letter-spacing: 0.1em;
    }

  </style>

</div>