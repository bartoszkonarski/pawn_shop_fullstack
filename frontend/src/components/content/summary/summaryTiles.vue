<template>
    <div class="tiles-field">
        <div class="tiles-field-info">
           <p>Nazwa: {{name}}</p>
           <p>Marka: {{brand}}</p>  
           <p>Stan: {{state}}</p>
           <p>Informacje: {{info}}</p>
           <p>Cena zakupu: {{cost}}</p>
           <p>Pozostało dni: {{days}}</p>
           
            <button 
            @click="$emit('del',id)" 
            class="tiles-field-info-button">
                Odebrano
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
        props: ['name','cost','state','info','brand', 'days','id'],
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
        width:80%;
        height: 80%;
        background: #C2D7DD;
        margin: 20px;
        padding: 20px;
        border-radius: 10px;
    }
    .tiles-field-info-button{
        width: 20%;
        height: 14%;
        background: rgb(70, 44, 70);
        color: white;
        border-radius: 15px;
        transition: .4s;
    }
    .tiles-field-info-button:hover{
        background: rgb(153, 87, 153);
        color:black;
        border-radius: 5px;
    }
</style>