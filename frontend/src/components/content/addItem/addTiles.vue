<template>
    <div class="edit-tiles-field">
        <div class="edit-tiles-field-image">
            <input type="image" class="edit-tiles-input-image">
        </div>
        <div class="edit-tiles-field-info">
            <label for="" class="edit-tites-label">Nazwa: 
                <input type="text" class="edit-tiles-input">
            </label> <br>

            <label for="" class="edit-tites-label">Marka: 
                <input type="text" class="edit-tiles-input">
            </label> <br>

            <label for="" class="edit-tites-label">Stan: 
                <input type="text" class="edit-tiles-input">
            </label> <br>

            <label for="" class="edit-tites-label">Informacje: 
                <input type="text" class="edit-tiles-input">
            </label> <br>

            <label for="" class="edit-tites-label">Cena zakupu: 
                <input type="number" class="edit-tiles-input">
            </label> <br>
            
            <label for="" class="edit-tites-label">Aktualna cena: 
                <input type="number" class="edit-tiles-input">
            </label> <br>
        </div>
    </div>
</template>

<script>

export default {
  name: 'tiles',
  components: {
  },
  data: function () {
    return {
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
</style>