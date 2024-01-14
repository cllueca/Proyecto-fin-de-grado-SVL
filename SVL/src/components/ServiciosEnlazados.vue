<template>
  <div v-if="this.$store.state.serviciosEnlazados != null" v-for="servicio in this.$store.state.serviciosEnlazados">
    <button class="botonServicio" :id="'boton' + servicio.id" @click="mostrarInfo(servicio.id)">
      <div class="nombreServicio">
        {{ servicio.nombre }}
        <span class="flechaServicio">
          <i class="fa-solid fa-arrow-down"></i>
        </span>
      </div>
    </button>
    <div class="container infoServicio hidden" :id="'info' + servicio.id">
      <div class="row">
        <div class="col-sm-12 col-lg-12">
          <span>Ultimo inicio de sesi&oacute;n:</span> {{ servicio.ultimo_login }}
        </div>
        <div class="col-sm-12 col-lg-12">
          <span>Enlazado:</span> {{ servicio.fecha_enlace }}
        </div>
        

        <div class="row">
          <div class="col-sm-12 col-lg-12" style="width: 96%; margin-left: 5%; margin-top:10px;">
            <a :href="servicio.url" target="_blank">
              <button class="botonEnlace">
                Ir a la web
              </button>
            </a>
          </div>
        </div>
      </div>  
    </div>
  </div>
  <div v-else>
    No hay servicos enlazados
  </div>
</template>

<style>

.botonServicio{
  width: 70%;
  margin-left: 15%;
  margin-top: 10px;
  padding: 0.5rem;
  border: solid 2px black;
  border-radius: 10px;
  background: #6A1B9A;
  color:#fff;
  outline: 0;
  font-size: 1rem;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}

.botonServicio:hover {
  background: rgba(106, 27, 154, 0.9);
}

.nombreServicio{
  position: relative;
  margin-left: -15%;
	flex: 1;  
}

.flechaServicio{
	margin-left: 50%;
}

.hidden{
  display: none;
}

.infoServicio{
width: 60%;
margin-left: 20%;
border-width: 0px 2px 2px 2px;
border-style: solid;
border-color: black;
color: black;
padding: 0.5rem;
}

.infoServicio span{
  font-weight: bold;
  text-decoration: underline;
}

.botonEnlace{
width: 100%;
font-weight: bold;
color: black;
border-radius: 10px;
}


@media (min-width: 900px) and (max-width: 1000px){
  .nombreServicio{
    margin-left: -10%;
  }
}

@media (min-width: 400px) and (max-width: 580px) {
  .nombreServicio{
    margin-left: -10%; 
  }
  .flechaServicio{
    margin-left: 40%;
  }
}

@media (min-width: 360px) and (max-width: 399px)
{
  .nombreServicio{
    margin-left: -5%;
  }
  .flechaServicio{
    margin-left: 30%;
  }
}

@media (max-width: 359px)
{
  .nombreServicio{
    margin-left: -2%;
  }
  .flechaServicio{
    margin-left: 10%;
  }
}

@media (max-width: 400px) {
  .botonServicio{
    width: 100%;
    margin-left: 0px;
  }

  .infoServicio{
    width: 94%;
    margin-left: 3%;
    font-size: 0.8rem;
  }
}
</style>

<script>
import store from '../store/index'
export default {
  methods:
  {
    mostrarInfo(id)
    {
      var boton = document.getElementById('boton' + id);
      var info = document.getElementById('info' + id);
      var flecha = boton.children[0].children[0].children[0];

      info.classList.toggle('hidden');

      if (flecha.classList.contains('fa-arrow-down'))
      {
        flecha.classList.remove('fa-arrow-down');
        flecha.classList.add('fa-arrow-up');
      }
      else
      {
        flecha.classList.add('fa-arrow-down');
        flecha.classList.remove('fa-arrow-up');
      }
    }
  }
}
</script>