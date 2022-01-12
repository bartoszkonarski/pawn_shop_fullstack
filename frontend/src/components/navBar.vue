<template>
  <section 
  class="nav-container"
  :class="{'nav-container-div': !logged}"
  >
    <div class="nav-logo" >
      <img src="../../src/assets/lombard-logo.png" alt="" :class="{'nav-logo-img': !logged}">
    </div>
    
    <div class="nav-link-container" v-show="logged">

      <router-link to="/">
        <div class="nav-tab" style="background-color: #96F04D">
          <font-awesome-icon icon="fa-solid fa-basket-shopping" />
        </div>
      </router-link>

      <router-link to="/add">
        <div class="nav-tab" style="background-color: #50D98E">
          <!-- <font-awesome-icon icon="fa-duotone fa-hexagon-plus" /> -->
        </div>
      </router-link> 

      <router-link to="/summary">
        <div class="nav-tab" style="background-color: #E6D149">
          <!-- <font-awesome-icon icon="fa-solid fa-calendar-circle-exclamation" /> -->
        </div>
      </router-link>
    </div>
    <div class="nav-user-accond" v-show="logged">
      <div class="nav-accond-info">
        {{accondName}}      
        <button 
        style="background-color: #EB714F; width:80%"
        @click="$emit('logOut')"
        >
            LogOut
            <!-- <font-awesome-icon icon="fa-solid fa-calendar-circle-exclamation" /> -->
        </button>
      </div>

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
  props:['logged'],
  data: () => {
      return{
        addItem: addItem,
        listItem: listItem,
        accondName:"user_name"
      }
  },
}
</script>

<style scoped>
.nav-container{
  background-color: #6666FF;
  height: 16vh;
}
.nav-link-container{
  float: left;
  width: 50vw;
  height: 14vh;
}
.nav-tab{
  display: block;
  background: red;
  color: black;
  font-size: 6vh;
  width: 20%;
  height: 50%;
  margin: 3% 5%;
  float: inline-start;
  text-align: center;
  border-radius: 15px;
  box-shadow: -1px 15px 60px 0px rgba(0,0,0,0.75);
  -webkit-box-shadow: -1px 15px 60px 0px rgba(0,0,0,0.75);
  -moz-box-shadow: -1px 15px 60px 0px rgba(0,0,0,0.75);
}
.nav-logo{
  float: left;
}
.nav-user-accond{
  float: left;
  width: 15vw;
  height: 14vh;
  text-align: center;
  align-items: center;

}
.nav-accond-info{
  background:#4DC8F0;
  width: 70%;
  height: 60%;
  border: solid 2px #663EFF;
  border-radius: 25px;
  text-align: center;
  vertical-align: middle;
  padding: 10px;
  margin-top: 5%;
}
.nav-container-div{
  height: 40vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.nav-logo-img{
  margin-top:20%;
  transform: scale(2);
}
img{
  width: 30vw;
  height: 14vh;
}
router-link{
 border-top: solid 4px white;
}
</style>
