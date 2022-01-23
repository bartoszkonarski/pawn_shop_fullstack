<template>
    <div class="edit-tiles-field">
        <div class="edit-tiles-field-info">
            <label for="" class="edit-tites-label" >Nazwa: 
                <input 
                type="text" 
                class="edit-tiles-input"
                v-model="newItem.name"
                v-on:input="$emit('info',newItem)"
                >
            </label> <br>

            <label for="" class="edit-tites-label">Marka: 
                <input 
                type="text" 
                class="edit-tiles-input"
                v-model="newItem.brand"
                v-on:input="$emit('info',newItem)"
                >
            </label> <br>

            <label for="" class="edit-tites-label">Stan: 
                <input 
                type="text"
                class="edit-tiles-input"
                v-model="newItem.state"
                v-on:input="$emit('info',newItem)"
                >
            </label> <br>

            <label for="" class="edit-tites-label">Informacje: 
                <input 
                type="text" 
                class="edit-tiles-input"
                v-model="newItem.info"
                v-on:input="$emit('info',newItem)"
                >
            </label> <br>

            <label for="" class="edit-tites-label">Cena zakupu: 
                <input 
                type="number" 
                class="edit-tiles-input"
<<<<<<< HEAD
                v-model="newItem.deposit"
=======
                v-model="newItem.cost"
>>>>>>> fb7405a (Fixed summary)
                v-on:input="$emit('info',newItem)"
                >
            </label> <br>

            <button 
            class="edit-tiles-button"
            @click="$emit('addClick')"
            >
                <b>Zastaw!</b> 
            </button>
        </div>
    </div>
</template>

<script>

export default {
  name: 'addTiles',
  components: {
  },
  data: function () {
    return {
<<<<<<< HEAD
        newItem: {name: '', deposit: 0, state: '', info: '', brand: ''}
=======
        newItem: {name: '', cost: '', state: '', info: '', brand: ''}
>>>>>>> fb7405a (Fixed summary)
    }
  },
//   methods: {
//         functi: function() {
//             console.log(this.newItem.name);
//       }
//   },
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
    }
    .edit-tiles-input:focus{
        outline: none !important;
        border-bottom: 2px solid #455de6;
        width:100%;
        transition: .5s;
    }
    .edit-tiles-field-info-button:hover{
        background: rgb(153, 87, 153);
        color:black;
        border-radius: 5px;
    }
    .edit-tiles-button{
        background: #579949;
        color:white;
        border: none;
        margin-top: 30px;
        height: 7vh;
        width: 7vh;
        border-radius: 100%;
        transition: .3s;
    }
    .edit-tiles-button:hover{
        background: #2a8f16;
        border: 1px solid;
        transition: .3s;
    }
    .edit-tiles-button:active{
        background: #156b04;
        border: 1px solid;
        height: 6vh;
        width: 6vh;
        transition: .3s;
    }
</style>