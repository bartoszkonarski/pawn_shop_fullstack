<template>
  <section>

      <div class="list-left-panel">
        
      </div>

      <div class="list-right-panel">
        <div class="list-field" v-for="i in 25" :key="i">
          
        </div>
        <br>
      </div>

  </section>
</template>

<script>

export default {
  name: 'listItem',
  components: {

  }
}
</script>
 
<style >
  .list-left-panel{
    display: flex;
    position: fixed;
    width:35%;
    height: 84vh;
    background: red;
    float:left;
  }
  .list-right-panel{
    display: flex;
    flex-direction:column;
    align-items: center;
    position: relative;
    left: 35%;
    margin: 0;
    padding: 4% 2%;
    background: yellow; 
    width:61%; 
  }
  .list-field{
    height: 200px;
    width: 300px;
    margin: 20px;
    background: violet;
  }
</style>
