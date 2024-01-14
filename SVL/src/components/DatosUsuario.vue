<template>
    <div class="col-md-12 border-right" id="inicioSeccion">
        <div class="p-3 py-5">
            <div class="row mt-2">
                <div class="col-md-12">
                    <i class="fa-solid fa-pen-to-square"></i><label class="labels">Nombre</label>
                    <input type="text" class="form-control" v-model="nombreValue">
                </div>
                <div class="col-md-12">
                    <i class="fa-solid fa-pen-to-square"></i><label class="labels">Apellidos</label>
                    <input type="text" class="form-control" v-model="apellidosValue">
                </div>
                <div class="col-md-12">
                    <label class="labels">Correo</label>
                    <input type="text" class="form-control" :value="correoValue" readonly="true">
                </div>
            </div>
            
            
            <div class="mt-5 text-center">
                <button class="btn btn-primary profile-button" type="button" @click="editarPerfil">Guardar cambios</button>
            </div>
        </div>
    </div>

</template>

<style>

.profile-button {
    background: #125E24;
    box-shadow: none;
    border: none
}

.profile-button:hover {
    background: rgba(16, 117, 69, 0.9);
}

.profile-button:focus {
    background: rgba(16, 117, 69, 0.9);
    box-shadow: none
}

.profile-button:active {
    background: rgba(16, 117, 69, 0.9);
    box-shadow: none
}

.labels {
    font-size: 20px;
}

@media (max-width: 400px) {

    #inicioSeccion{
        margin-top: -60px;
    }
}
</style>

<script>
import store from '../store/index'
export default{
    data() {
      return {
          nombreValue: '',
          apellidosValue: '',
          correoValue: '',
      };
    },
    created() {
        this.nombreValue = this.nombre;
        this.apellidosValue = this.apellidos;
        this.correoValue = this.correo;
    },
    computed:{
        nombre(){
            return $cookies.get('auth')['usuario']['nombre'];
        },
        apellidos(){
            return $cookies.get('auth')['usuario']['apellidos'];
        },
        correo(){
            return $cookies.get('auth')['usuario']['correo'];
        }
    },
    methods:{
        async editarPerfil()
        {
            if((this.nombreValue == this.nombre) && (this.apellidosValue == this.apellidos))
            {
                alert("No se ha cambiado nada");
            }
            else
            {
                let jsonData = {
                    nombre: this.nombreValue,
                    apellidos: this.apellidosValue
                }

                try {
                    await store.dispatch("doUpdate", jsonData);
                } catch (error) {
                    console.error(error);
                }
            }
        }
    }
}

</script>