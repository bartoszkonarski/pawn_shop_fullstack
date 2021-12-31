<template>
    <div class="tiles-field">
        <div class="tiles-field-image">
           <img src="" alt="">
        </div>
        <div class="tiles-field-info">
           <p>Nazwa: {{name}}</p>
           <p>Marka: {{brand}}</p>  
           <p>Stan: {{state}}</p>
           <p>Informacje: {{info}}</p>
           <p>Cena zakupu: {{cost}}</p>
           <p>Aktualna cena: {{newCost}}</p>
            <button 
            @click="$emit('edit')" 
            class="tiles-field-info-button">
                Edycja
            </button>
        </div>
    </div>
</template>

<script>

export default {
  name: 'tiles',
  components: {
  },
  emits: ['accepted'],
  props: ['name','cost','state','info','brand','newCost','id'],
  data: function () {
    return {
    }
  }
}
</script>

<style scoped>
    .tiles-field{
        display: flex;
        flex-direction:row;
        align-items: center;
        height: 300px;
        width: 80%;
        margin: 20px;
        padding: 10px;
        background: #0A4657;
    }
    .tiles-field-image{
        width:40%;
        height: 100%;
        background:black;
    }
    .tiles-field-info{
        width:50%;
        height: 80%;
        background: #C2D7DD;
        margin: 20px;
        padding: 20px;
        border-radius: 10px;
    }
    .tiles-field-info-button{

    }
</style>