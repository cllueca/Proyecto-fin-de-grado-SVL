<script setup>
import DatosUsuario from '../components/DatosUsuario.vue';
import ServiciosDisponibles from '../components/ServiciosDisponibles.vue';
import ServiciosEnlazados from '../components/ServiciosEnlazados.vue';
</script>


<template>
    <div class="container">
        <div class="profile-header">

            <div class="profile-nav-info">
                <h3 class="user-name">{{ username }}</h3>
                <div class="address">
                    <p id="state" class="state">Activo desde: </p>
                    <span id="country" class="country">{{ fecha_registro }}</span>
                </div>
            </div>
        </div>

        <div class="main-bd">
          <div class="left-side">
              <div class="profile-side">
                <button id="botonDesplegable" class="hamburguesa" @click="toggleMenu()"><i class="fas fa-bars" id="btnIcon"></i></button>
                  <div class="profile-btn left-side-hide" id="opcionesPerfil">
                      <button class="perfilbtn activeButton tabBtn" id="datosTabB" @click="opcionesPerfil('datosTab')"><i class="fa fa-user"></i>Perfil</button>
                      <button class="linkedbtn tabBtn" id="linkedTabB" @click="opcionesPerfil('linkedTab')"><i class="fa fa-lock"></i>Servicios enlazados</button>
                      <button class="unlinkedbtn tabBtn" id="avTabB" @click="opcionesPerfil('avTab')"><i class="fa fa-plus"></i>Servicios sin enlazar</button>
                      <button class="logoutbtn" @click="cerrarSesion"><i class="fa-solid fa-right-from-bracket"></i>Salir</button>
                  </div>
              </div>

          </div>
          
          <div class="right-side">
      
          <div class="profile-body">
              <div id="datosTab" class="profile-posts tab show">
                  <h1>Datos del perfil</h1>
                  <hr>
                  <DatosUsuario />
              </div>

              <div id="linkedTab" class="profile-reviews tab">
                  <h1>Servicios enlazados</h1>
                  <hr>
                  <ServiciosEnlazados />
              </div>

              <div id="avTab" class="profile-settings tab">
                  <div class="account-setting">
                      <h1>Posibles enlaces</h1>
                      <hr>
                      <ServiciosDisponibles />
                  </div>
              </div>
          </div>
        </div>
    </div>
    </div>
    
</template>


<style>

@import url("https://fonts.googleapis.com/css?family=Poppins&display=swap");
@import url("https://fonts.googleapis.com/css?family=Bree+Serif&display=swap");

#botonDesplegable {
  display: none;
}

.hamburguesa {
  padding: 10px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 20px;
}

.hamburguesa i {
  color: #000;
}

.activeButton{
    background-color:#125E24 !important;
}

.profile-header {
  background: #fff;
  width: 100%;
  display: flex;
  height: 190px;
  position: relative;
  box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.2);
}

.profile-nav-info {
    margin-left:5%;
    float: left;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-top: 60px;
}

.profile-nav-info h3 {
  font-variant: small-caps;
  font-size: 2rem;
  font-family: sans-serif;
  font-weight: bold;
}

.profile-nav-info .address {
  display: flex;
  font-weight: bold;
  color: #777;
}

.profile-nav-info .address p {
  margin-right: 5px;
}

.main-bd {
  width: 100%;
  display: flex;
  padding-right: 15px;
}

.profile-side {
  width: 300px;
  background: #fff;
  box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);
  padding: 20px 30px 20px;
  font-family: "Bree Serif", serif;
  margin-left: 10px;
  z-index: 99;
}

button.perfilbtn,
button.linkedbtn,
button.unlinkedbtn,
button.logoutbtn {
  border: 0;
  padding: 10px;
  width: 100%;
  border-radius: 10px;
  background: #24AB43;
  color: #fff;
  font-family: "Bree Serif";
  font-size: 1rem;
  margin: 5px 2px;
  cursor: pointer;
  outline: none;
  margin-bottom: 10px;
  transition: background 0.3s ease-in-out;
  box-shadow: 0px 5px 7px 0px rgba(0, 0, 0, 0.3);
}

button.perfilbtn:hover,
button.linkedbtn:hover,
button.unlinkedbtn:hover,
button.logoutbtn:hover {
  background: rgba(16, 117, 69, 0.9);
}

button.perfilbtn i,
button.linkedbtn i,
button.unlinkedbtn i,
button.logoutbtn i {
  margin-right: 5px;
}

.right-side{
    width: 100%;
}

.nav {
  width: 100%;
  z-index: -1;
}

.nav ul {
  display: flex;
  justify-content: space-around;
  list-style-type: none;
  height: 40px;
  background: #fff;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
}

.nav ul li {
  padding: 10px;
  width: 100%;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s ease-in-out;
}

.nav ul li:hover,
.nav ul li.active {
  box-shadow: 0px -3px 0px rgba(288, 0, 70, 0.9) inset;
}

.profile-body {
  width: 100%;
  z-index: -1;
}

.profile-btn{
  border-radius: 10px;
}

.tab {
  display: none;
  padding: 20px;
  width: 100%;
  text-align: center;
}

.show{
  display: block;
}

.left-side-hide{
  display: block;
}

/* mediaquerys para el boton desplegable */
@media screen and (max-width: 800px) {
  .left-side-hide {
    display: none;
  }

  #botonDesplegable {
    display: block;
  }
}

/**/
@media (max-width: 1100px) {
  .profile-side {
    width: 250px;
    padding: 20px 15px 20px;
  }
}

@media (max-width: 900px) {
  body {
    margin: 0 20px;
  }

  .profile-header {
    display: flex;
    height: 100%;
    flex-direction: column;
    text-align: center;
    padding-bottom: 20px;
  }

  .profile-nav-info {
    text-align: center;
  }

  .main-bd {
    flex-direction: column;
    padding-right: 0;
  }

  .profile-side {
    width: 100%;
    text-align: center;
    padding: 20px;
    margin: 5px 0;
  }

  .profile-nav-info .address {
    justify-content: center;
  }
}

@media (max-width: 400px) {

  .profile-nav-info h3 {
    font-size: 1.9rem;
  }

  .profile-nav-info .address p,
  .profile-nav-info .address span {
    font-size: 0.7rem;
  }

  #datosTab h1{
    margin-top: -10px;
  }

  #linkedTab h1{
    margin-top: -10px;
  }

  #avTab h1{
    margin-top: -10px;
  }
}

.tab h1 {
  font-family: "Bree Serif", sans-serif;
  display: flex;
  justify-content: center;
  margin: 20px auto;
}



</style>

<script>

export default {
  computed:{
      username(){
          var cookieData = $cookies.get('auth')
          return cookieData['usuario']['nombre'];
      },
      fecha_registro(){
        var cookieData = $cookies.get('auth');
        return cookieData['usuario']['fecha_registro'];
      }
  },
  methods:{
    async cerrarSesion(){
        try{  
          await this.$store.dispatch("doLogout");
        } catch (error) {
            console.error(error);
        }
    },
    async opcionesPerfil(idTab){
      var boton = document.getElementById(idTab + 'B');
      var tab = document.getElementById(idTab);
      var activeBtn = document.querySelector('.activeButton');
      var activeTab = document.querySelector('.show');

      if(idTab == 'linkedTab')
      {
        try{
          await this.$store.dispatch("doGetLinkedServices");
        }
        catch (error){
          console.log(error);
        }
      }

      if(idTab == 'avTab')
      {
        try{
          this.$store.dispatch("doGetAvailableServices");
        }
        catch(error)
        {
          console.log(error);
        }
        
      }

      activeBtn.classList.remove('activeButton');
      activeTab.classList.remove('show');

      boton.classList.add('activeButton');
      tab.classList.add('show');

      this.toggleMenu();
    },
    toggleMenu()
    {
      const mostrarOcultarBtn = document.getElementById('botonDesplegable');
      const miDiv = document.getElementById('opcionesPerfil');
      const icono = document.getElementById('btnIcon');

      miDiv.classList.toggle('left-side-hide');
      mostrarOcultarBtn.classList.toggle('rotated');

      if (icono.classList.contains('fa-bars'))
      {
        icono.classList.add('fa-times');
        icono.classList.remove('fa-bars');
      }
      else
      {
        icono.classList.remove('fa-times');
        icono.classList.add('fa-bars');
      }
    }
  }
}
</script>