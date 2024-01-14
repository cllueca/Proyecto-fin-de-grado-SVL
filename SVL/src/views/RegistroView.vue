<template>
    <div class="container mt-5">
        <div class="row d-flex justify-content-center align-items-center" id="divContenedorForm">
            <div class="col-md-8">
                <form id="regForm">
                    <h1 id="register">Registrarse</h1>

                    <div v-if="this.$store.state.messageReg == null" id="errorVoz" class="hide"></div>
                    <div v-else id="errorVoz">{{ this.$store.state.messageReg }}</div>

                    <div class="all-steps" id="all-steps"> 
                        <span class="step"><i class="fa fa-envelope"></i></span>
                        <span class="step"><i class="fa fa-user"></i></span>
                        <span class="step"><i class="fa fa-lock"></i></span>
                    </div>

                    <div class="tab" style="display: block;">
                        <h5>¿Quien eres?</h5>
                        <p>
                            <input placeholder="Correo electrónico" type="text" class="form-control form-control-lg" name="email" v-model="correo">
                        </p>
                    </div>

                    <div class="tab" style="display: none;">
                      <h5>Danos un poco m&aacute;s de informaci&oacute;n sobre ti:</h5>
                      <p>
                        <input placeholder="Nombre" type="text" class="form-control form-control-lg" name="nombre" v-model="nombre">
                      </p>
                      <p>
                        <input placeholder="Apellidos" type="text" class="form-control form-control-lg" name="apellidos" v-model="apellidos">
                      </p>
                    </div>

                    <div class="tab" style="display: none;">
                        <h5>
                            Para terminar el proceso, crea una contraseña utilizando <span id="opcionPwd">tu voz</span>:
                        </h5>

                        <div id="botonCambio">
                            <button id="pwdBtn" type="button" class="btn btn-outline-secondary" @click="cambiarTipoPwd">
                                <span>
                                    <i id="flechasCambio" class="fa fa-arrows-rotate"></i>
                                </span>
                                Cambiar
                            </button>
                        </div>
                        
                        <p id="inputTxt" class="hide" style="margin-top: 10px;">
                            <input type="password" class="form-control form-control-lg" name="textPwd" placeholder="Password..." v-model="normal_password">
                        </p>

                        <div id="inputVoz" class="form-group">
                            <div class="row input-group mb-3">
                                <p style="font-size: 1.5rem;"><strong>Pulsa el circulo y habla hasta que se llene:</strong></p>
                                <p>Por si te quedas sin ideas...</p>
                                <ul class="listaIdeas"> - ¿Qu&eacute; tiempo hace?</ul>
                                <ul class="listaIdeas"> - ¿Qu&eacute; hiciste ayer?</ul>
                                <ul class="listaIdeas"> - ¿Qu&eacute; llevas puesto?</ul>
                                <button type="button" id="recordButton" @click="startRecording">
                                    <i id="micIcon" class="fa-solid fa-microphone fa-xl" style="color: #000000;"></i>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div style="overflow:auto;" id="nextprevious">
                        <div style="float:right;" class="flechasMoverse">
                            <button type="button" id="prevBtn1" @click="changeTab(-1)"><i class="fa fa-angle-double-left"></i></button> 
                            <button type="button" id="nextBtn" @click="changeTab(1)"><i class="fa fa-angle-double-right"></i></button> 
                        </div>
                        <div style="float:left" class="flechaInicio">
                            <button type="button" style="overflow:auto; float:left;" class="btn btn-light" @click="this.$router.go(-1)" ><i class="fa-sharp fa-solid fa-arrow-left"></i> P&aacute;gina principal</button>
                        </div>
                    </div>

                    <div id="enviar" style="overflow:auto; display:none;">
                        <div style="float:right;" class="flechasMoverse">
                            <button type="button" id="prevBtn2" @click="changeTab(-1)"><i class="fa fa-angle-double-left"></i></button> 
                            <button type="submit" id="sendBtn" @click.prevent="sendData">enviar</button>
                        </div>
                        <div style="float:left" class="flechaInicio">
                            <button type="button" style="overflow:auto; float:left;" class="btn btn-light" @click="this.$router.go(-1)" ><i class="fa-sharp fa-solid fa-arrow-left"></i> P&aacute;gina principal</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>


<style>

body {
    background: #eee
}

#errorVoz{
    background-color: rgba(255, 0, 0, 0.5);
    width: 100%;
    text-align: center;
    font-size: 1.5rem;
    font-weight: bold;
    border-radius: 20px;
}

#regForm {
    background-color: #ffffff;
    margin: 0px auto;
    font-family: Raleway;
    padding: 40px;
    border-radius: 10px
}

#register{
  color: #6A1B9A;
}

h1 {
    text-align: center
}

h5{
    text-align: center;
    margin-bottom: 20px;
}

#botonCambio{
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

input {
    padding: 10px;
    width: 100%;
    font-size: 17px;
    font-family: Raleway;
    border: 1px solid #aaaaaa;
    border-radius: 10px;
}



.tab input:focus{

  border:1px solid #6a1b9a !important;
  outline: none;
}

input.invalid {
 
    border:1px solid #e03a0666;
}

#prevBtn1, #prevBtn2, #nextBtn, #sendBtn {
    background-color: #6A1B9A;
    color: #ffffff;
    border: none;
    border-radius: 50%;
    padding: 10px 20px;
    font-size: 17px;
    font-family: Raleway;
    cursor: pointer
}

#prevBtn1:hover, #prevBtn2:hover, #nextBtn:hover, #sendBt:hover {
    opacity: 0.8
}

#prevBtn1:focus, #prevBtn2:focus, #nextBtn:focus, #sendBt:focus{

  outline: none !important;
}

#prevBtn1, #prevBtn2 {
    background-color: #bbbbbb
}


.all-steps{
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px;
    width: 100%;
    display: inline-flex;
    justify-content: center;
}

.step {
    height: 40px;
    width: 40px;
    margin: 0 2px;
    background-color: #bbbbbb;
    border: none;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 15px;
    color: #6a1b9a;
    opacity: 0.5;
}

.step.active {
    opacity: 1
}

.step.finish {
   color: #fff;
   background: #6a1b9a;
   opacity: 1;

}

.all-steps {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px
}

/* ---------------------------------------------- */

.registerForm{
    width: 70%;
    height: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform:translate(-50%,-50%);
    background: #f3f3f3;
    box-shadow: 1px 1px 4px #dcdcdc;
}

.hide {
    opacity: 0;
    transition: opacity 1s ease-in-out;
    display: none;
    /* opacity: 0;
    visibility: hidden;
    height: 0;
    overflow: hidden;
    transition: opacity 1s ease-in-out, height 0s ease-in-out 1s; */
}


#tituloRegister{
    text-align: center;
    font-size: 44px;
    text-decoration:underline;
    font-weight: bold;
}

#pwdBtn{
    color:black;
}

#flechasCambio {
  transition: transform 1s ease-in-out; /* Agregar regla de transición */
}

.rotar {
  transform: rotate(360deg);
}


#recordButton{
  display: block;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin: 0 auto;

}

.listaIdeas{
    padding-left: 10%;
}

.pie-wrap {
	height: 100px;
	width: 100px;
	position: relative;
	overflow: hidden;
	margin: 20px;
	border-radius: 50%;
	transform: rotate3d(0, 0, 1, 0.001deg); /* clear artifacts*/
}
.pie-wrap:before,
.pie-wrap:after {
	content: " ";
	position: absolute;
	left: 0;
	top: 0;
	width: 100px;
	height: 100px;
	clip: rect(0px, 50px, 100px, 0px);
	background-color: #f3f3f3;
	transform: rotate3d(0, 0, 1, 0deg);
	animation: 0.5s spin2 linear 1s forwards;
	z-index: 2;
}
.pie-wrap:after {
	content: " ";
	background: #6A1B9A;
	z-index: 1;
	animation: 1s spin linear 0s forwards;
}

@keyframes spin {
	from {
		transform: rotate3d(0, 0, 1, 0deg);
	}
	to {
		transform: rotate3d(0, 0, 1, 180deg);
	}
}
@keyframes spin2 {
	from {
		background: #6A1B9A;
		transform: rotate3d(0, 0, 1, 180deg);
	}
	to {
		background: #6A1B9A;
		transform: rotate3d(0, 0, 1, 360deg);
	}
}

@media (max-width: 400px)
{
    #regForm {
        padding: 20px;
    }

    h5{
        text-align: center;
        margin-bottom: 20px;
    }

    #botonCambio{
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
    }

    #pwdBtn{
        justify-content: center;
    }

    .flechasMoverse{
        width: 100%;
        display: flex;
        justify-content: center;
    }

    .flechasMoverse button{
        margin: 10px;
    }

    .flechaInicio{
        margin-top: 30px;
        width: 100%;
    }

    .all-steps{
        margin-top: 10px;
        margin-bottom: 15px;
    }

    #divContenedorForm{
        margin-top: -5%;
    }
}
</style>


<script>
import store from '../store/index'
export default {
    data() {
      return {
          correo: '',
          nombre: '',
          apellidos: '',
          voice_password: null,
          normal_password: null,

          recording: false,
          stream: null,
          recorder: null,

          currentTab: 0
      }
    },
    async mounted(){
        await this.cogerMicro();
    },
    methods: {
        async cogerMicro()
        {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                console.log('Acceso al micrófono concedido');
                // Aquí puedes hacer algo con el flujo de audio, como reproducirlo o grabarlo
            } catch (error) {
                console.log('No se pudo acceder al micrófono:', error);
            }
        },
        cambiarTipoPwd() {
            const flechas = document.getElementById('flechasCambio');
            const botonCambio = document.getElementById('pwdBtn');
            const inputVoz = document.getElementById('inputVoz');
            const inputTxt = document.getElementById('inputTxt');
            const textoPwd = document.getElementById('opcionPwd');


            flechas.classList.toggle('rotar');

            if(textoPwd.textContent == 'tu voz')
            {
                textoPwd.textContent="texto";
            }
            else
            {
                textoPwd.textContent="tu voz";
            }
    
            if (inputVoz.classList.contains('hide')) {
                inputVoz.classList.remove('hide');
                inputTxt.classList.add('hide');
            } else {
                inputTxt.classList.remove('hide');
                inputVoz.classList.add('hide');
            }
        },
        startRecording() {
            navigator.mediaDevices.getUserMedia({ audio: true })
            .then((stream) => {
                
                const botonGrabar = document.getElementById("recordButton");
                const icono = document.getElementById("micIcon");
                botonGrabar.classList.add('pie-wrap');
                icono.classList.add('hide');

                this.recording = true;
                this.stream = stream;
                this.recorder = new MediaRecorder(stream);
                this.recorder.start();
                this.recorder.ondataavailable = (event) => {
                let blob = new Blob([event.data], { type: 'audio/mp3' });
                this.voice_password = blob;//window.URL.createObjectURL(blob);
                // Aquí puedes guardar el archivo WAV en el servidor o enviarlo a otra parte de tu aplicación
                };
                // Detener la grabación después de 5 segundos
                setTimeout(() => {
                    botonGrabar.classList.remove('pie-wrap');
                    icono.classList.remove('hide');  
                    this.stopRecording();
                }, 1500);
            })
            .catch((err) => {
                console.log('No se ha podido acceder al micrófono', err);
            });
        },
        stopRecording() {
            if (this.recording) {
            this.recorder.stop();
            this.recording = false;
            this.stream.getTracks().forEach((track) => track.stop());
            }
        },
        downloadAudio() {
            let link = document.createElement('a');
            link.href = this.voice_password;
            link.download = 'grabacion.mp3';
            link.click();
        },
        async sendData() {

            if (this.existePwd())
            {
            var jsonData = { nombre: this.nombre,
                            correo: this.correo,
                            apellidos: this.apellidos,
                            normal_password: this.normal_password };

            if (this.voice_password != null)
            {
                this.getBlobBase64Data(this.voice_password).then((base64Data) => {
                    // Agregar la cadena base64 al objeto JSON
                    jsonData.voice_password = base64Data;
                    try {
                        store.dispatch("doRegister", jsonData);
                    } catch (error) {
                        console.error(error);
                    }
                });
            }
            else // Contraseña normal
            {
                jsonData.voice_password = this.voice_password;
                try {
                    await store.dispatch("doRegister", jsonData);
                } catch (error) {
                    console.error(error);
                }
            }
            }
            else
            {
            console.log("No hay contraseña");
            }
        },
        existePwd(){
            if (this.voice_password == null && (this.normal_password == null || this.normal_password == '')){
            return false
            }
            else{
            return true
            }
        },
        getBlobBase64Data(blob) {
            return new Promise((resolve, reject) => {
                var reader = new FileReader();
                reader.readAsArrayBuffer(blob);
                reader.onload = function (event) {
                var binary = "";
                var bytes = new Uint8Array(event.target.result);
                var len = bytes.byteLength;
                for (var i = 0; i < len; i++) {
                    binary += String.fromCharCode(bytes[i]);
                }
                var base64Data = btoa(binary);
                resolve(base64Data);
                };
                reader.onerror = reject;
            });
        },
        changeTab(dir){
            var x = document.getElementsByClassName("tab");
            var valid = false;

            if ((dir == -1 && this.currentTab > 0) || dir == 1){
                    valid = true;
            }

            if(valid){
                if (dir == 1 && !this.validateForm()) return false;

                x[this.currentTab].style.display = "none";
                this.currentTab = this.currentTab + dir;
                x[this.currentTab].style.display = "block";
                this.fixStepIndicator(this.currentTab);

                if (this.currentTab == (x.length - 1)) {
                    document.getElementById("nextprevious").style.display = "none";
                    document.getElementById("enviar").style.display="block";
                }
                else
                {
                    document.getElementById("nextprevious").style.display = "block";
                    document.getElementById("enviar").style.display="none";
                }
            }
        },
        validateForm() {
            var x, y, i, valid = true;
            x = document.getElementsByClassName("tab");
            y = x[this.currentTab].getElementsByTagName("input");
            for (i = 0; i < y.length; i++) {
                if (y[i].value == "") {
                    y[i].className += " invalid";
                    valid = false;
                }
            }
            if (valid) {
                document.getElementsByClassName("step")[this.currentTab].className += " finish";
            }
            return valid;
        }, 
        fixStepIndicator(n) {
            var i, x = document.getElementsByClassName("step");
            for (i = 0; i < x.length; i++) {
                x[i].className = x[i].className.replace(" active", "");
            }
            x[n].className += " active";
        }
    }
}
</script>