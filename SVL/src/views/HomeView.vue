<template>
    <main>
        <div class="container" id="mainC">
            <div class="row" id="textoInfo">
                <h1>Bienvenido al nuevo servicio de gestión de cuentas</h1>
                <hr>

                <div class="content-slider">
                    <div class="slider">
                        <div class="mask">
                            <ul>
                                <li class="anim1">
                                    <div class="quote">Olv&iacute;date de tener muchas contraseñas</div>
                                </li>
                                <li class="anim2">
                                    <div class="quote">Si&eacute;ntete seguro</div>
                                </li>
                                <li class="anim3">
                                    <div class="quote">Todo en un mismo sitio</div>
                                </li>
                                <li class="anim4">
                                    <div class="quote">Unifica y gestiona tus cuentas de manera sencilla</div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row" id="botones">
                <div class="col-lg-6 col-md-12 col-sm-12 text-center">
                    <button @click="this.$router.push('/inicioSesion')" class="button btn-primary" type="button" id="botonLogin">Iniciar Sesion</button>
                </div>
                <div class="col-lg-6 col-md-12 col-sm-12 text-center">
                    <button @click="this.$router.push('/registro')" class="button btn-primary" type="button" id="botonRegistro">Registrarse</button>
                </div>
            </div>
        </div>
    </main>
</template>


<style scoped>

    #mainC{
        width: 80%;
        height: 85vh;
    }

    #textoInfo{
        width: 80%;
        margin-left: 10%;
        margin-top: 5%;
        margin-bottom: 2%;
    }

    #botones{
        width: 80%;
        margin-left: 10%;
        margin-top: 10%;
    }

    #botonLogin,
    #botonRegistro {
        border: 0;
        padding: 10px;
        width: 100%;
        height: 25vh;
        border-radius: 10px;
        background: #6A1B9A;
        color: #fff;
        font-family: "Bree Serif";
        font-size: 2rem;
        cursor: pointer;
        outline: none;
        margin-bottom: 10px;
        transition: background 0.3s ease-in-out;
        box-shadow: 0px 5px 7px 0px rgba(0, 0, 0, 0.3);
    }
    #botonLogin:hover,
    #botonRegistro:hover {
        background: rgba(147, 29, 220, 0.9);
    }

    h1 {
        text-align: center;
    }

    .content-slider {
        width: 100%;
    }

    .slider {
        width: 100%;
        
        overflow: visible;
        position: relative;
    }

    .mask {
        overflow: hidden;
        height: 100px;
    }

    .slider ul {
        margin: 0;
        padding: 0;
        position: relative;
    }

    .slider li {
        width: 100%;
        position: absolute;
        top: -325px;
        list-style: none;
    }

    .slider .quote {
        width: 100%;
        font-size: 30px;
        text-align: center;
        font-style: italic;
    }

    .slider li.anim1 {
    animation: cycle 20s linear infinite;
    }

    .slider li.anim2 {
    animation: cycle2 20s linear infinite;
    }

    .slider li.anim3 {
    animation: cycle3 20s linear infinite;
    }

    .slider li.anim4 {
    animation: cycle4 20s linear infinite;
    }

    .slider:hover li {
    animation-play-state: paused;
    }

    @keyframes cycle {
    0% {
        top: 0px;
    }
    4% {
        top: 0px;
    }
    16% {
        top: 0px;
        opacity: 1;
        z-index: 0;
    }
    20% {
        top: 325px;
        opacity: 0;
        z-index: 0;
    }
    21% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    50% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    92% {
        top: -325px;
        opacity: 0;
        z-index: 0;
    }
    96% {
        top: -325px;
        opacity: 0;
    }
    100% {
        top: 0px;
        opacity: 1;
    }
    }

    @keyframes cycle2 {
    0% {
        top: -325px;
        opacity: 0;
    }
    16% {
        top: -325px;
        opacity: 0;
    }
    20% {
        top: 0px;
        opacity: 1;
    }
    24% {
        top: 0px;
        opacity: 1;
    }
    36% {
        top: 0px;
        opacity: 1;
        z-index: 0;
    }
    40% {
        top: 325px;
        opacity: 0;
        z-index: 0;
    }
    41% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    100% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    }

    @keyframes cycle3 {
    0% {
        top: -325px;
        opacity: 0;
    }
    36% {
        top: -325px;
        opacity: 0;
    }
    40% {
        top: 0px;
        opacity: 1;
    }
    44% {
        top: 0px;
        opacity: 1;
    }
    56% {
        top: 0px;
        opacity: 1;
        z-index: 0;
    }
    60% {
        top: 325px;
        opacity: 0;
        z-index: 0;
    }
    61% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    100% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    }

    @keyframes cycle4 {
    0% {
        top: -325px;
        opacity: 0;
    }
    56% {
        top: -325px;
        opacity: 0;
    }
    60% {
        top: 0px;
        opacity: 1;
    }
    64% {
        top: 0px;
        opacity: 1;
    }
    76% {
        top: 0px;
        opacity: 1;
        z-index: 0;
    }
    80% {
        top: 325px;
        opacity: 0;
        z-index: 0;
    }
    81% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    100% {
        top: -325px;
        opacity: 0;
        z-index: -1;
    }
    }

    /* @media (max-width: 970px)
    {
        .content-slider {
            width: 100%;
        }

        .slider li {
            width: 680px;
            height: 320px;
            position: absolute;
            top: -325px;
            left: -200px;
            list-style: none;
        }

        .slider .quote {
            width: 100%;
            font-size: 20px;
        }
    } */


    /* Slider mediaquerys */
    @media (min-width: 550px) and (max-width: 700px)
    {
        .slider .quote {
            font-size: 25px;
        }
    }

    @media (min-width: 380px) and (max-width: 549px)
    {
        .slider .quote {
            font-size: 20px;
        }
    }

    @media (max-width: 379px)
    {
        .slider .quote {
            font-size: 15px;
        }

        #textoInfo h1{
            font-size: calc(1.3rem + 1.2vw);
        }

        #textoInfo{
            width: 90%;
            margin-left: 5%;
        }

        .content-slider{
            height: 70px;
        }

        #botones{
            margin-top: 0;
        }
    }

    /* Botones mediaquerys */
    @media (min-width: 601px) and (max-width: 991px)
    {
        #botonLogin,
        #botonRegistro {
            height: 20vh;
            font-size: 1.5rem;
            width: 80%;
        }

        #botonRegistro
        {
            margin-top: 5%;
        }
    }

    @media (min-width: 360px) and (max-width: 600px)
    {
        #botonLogin,
        #botonRegistro {
            height: 20vh;
            font-size: 1.5rem;
        }
    }

    @media (max-width: 359px)
    {
        #botonLogin,
        #botonRegistro {
            height: 15vh;
            margin-top: 10%;
            font-size: 1rem;
            margin-bottom: 5px;
        }
    }
</style>