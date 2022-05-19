<template>
    <div class="edit-tiles-field">
        <div class="edit-tiles-field-info">
            <label for="" class="edit-tites-label">Nazwa: 
                <input type="text" class="edit-tiles-input" v-model="item.name">
            </label> <br>

            <label for="" class="edit-tites-label">Marka: 
                <input type="text" class="edit-tiles-input" v-model="item.brand">
            </label> <br>

            <label for="" class="edit-tites-label">Stan: 
                <input type="text" class="edit-tiles-input" v-model="item.state">
            </label> <br>

            <label for="" class="edit-tites-label">Informacje: 
                <input type="text" class="edit-tiles-input" v-model="item.info">
            </label> <br>

            <label for="" class="edit-tites-label">Cena zakupu: 
                <input type="number" class="edit-tiles-input" v-model="item.cost">
            </label> <br>
            
            <label for="" class="edit-tites-label">Aktualna cena: 
                <input type="number" class="edit-tiles-input" v-model="item.newCost">
            </label> <br>

            <button 
            class="edit-tiles-button"
            @click="$emit('editClick', item)"
            > Edytuj </button>

            <button 
            class="edit-tiles-button"
            @click="$emit('cancelClick')"
            > Anuluj </button>
        </div>
    </div>
</template>

<script>

export default {
  name: 'tiles',
  props:['name','cost','state','info','brand','newCost','id'],
  components: {
  },
  data: function () {
    return {
        item: {name: this.name, cost: this.cost, state: this.state, info: this.info, brand: this.brand, newCost: this.newCost, id: this.id}
    }
  }
}
</script>

<style scoped>
    .edit-tiles-field{
        display: flex;
        flex-direction:column;
        align-items: center;
        height: 80%;
        width: 80%;
        margin: 20px;
        padding: 10px;
        background: #2826ac;
    }
    .edit-tiles-field-image{
        width:60%;
        height: 60%;
        background:black;
    }
    .edit-tiles-field-info{
        display: flex;
        flex-direction:column;
        align-items: center;
        width:85%;
        height: 100%;
        background: #C2D7DD;
        margin: 20px;
        padding: 20px;
        border-radius: 10px;
    }
    .edit-tiles-input{
        border-top: 0px;
        border-left: 0px;
        border-right: 0px;
        width:90%;
        border-bottom: 2px solid rgb(85, 84, 84);
        background: none;
        transition: .5s;
        font-size: 18px;
    }
    .edit-tiles-input:focus{
        outline: none !important;
        border-bottom: 2px solid rgb(69, 93, 230);
        width:100%;
        transition: .5s;
    }
    .edit-tiles-field-info-button:hover{
        background: rgb(153, 87, 153);
        color:black;
        border-radius: 5px;
    }
    .edit-tiles-button{
        display: inline;
        background: #7812a7;
        color:white;
        border: none;
        margin-top: 30px;
        height: 7vh;
        width: 7vh;
        border-radius: 100%;
        transition: .3s;
    }
    .edit-tiles-button:hover{
        background: #7812a7;
        border: 1px solid;
        transition: .3s;
    }
    .edit-tiles-button:active{
        background: #7812a7;
        border: 1px solid;
        height: 6vh;
        width: 6vh;
        transition: .3s;
    }
    .edit-tites-label{
        font-size: 25px;
        font-weight: bold;
    }
</style>