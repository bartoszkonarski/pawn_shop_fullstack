<template>
  <section 
  class="nav-container"
  >
    <div class="nav-logo">
      <img src="../../src/assets/lombard-logo.png" alt="">
    </div>
    
    <div class="nav-link-container">

      <router-link to="/">
        <div class="nav-tab">addItem</div>
      </router-link>

      <router-link to="/add">
        <div class="nav-tab">listItem</div>
      </router-link> 

      <router-link to="/summary">
        <div class="nav-tab">summary</div>
      </router-link>  

    </div>
    <div style="clear:both"></div>

    

  </section>
</template>

<script>
import addItem from './content/addItem.vue';
import listItem from './content/listItem.vue';
export default {
  name: 'navBar',
  components: {
  },
  data: () => {
      return{
        addItem: addItem,
        listItem: listItem,
      }
  },
}
</script>

<style scoped>
.nav-container{
  background-color: blue;
  height: 20vh;
}
.nav-link-container{
  float: left;
  width: 70vw;
  height: 14vh;
  
}
.nav-tab{
    display: block;
    height: 40px;
    width: 100px;
    margin:50px 100px;
    background: rgb(78, 41, 82);
    float: left;
    margin-top: 3vh;
}
.nav-logo{
  float: left;

}
img{
  width: 30vw;
  height: 14vh;
}
</style>
