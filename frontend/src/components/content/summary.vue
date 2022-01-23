<template>
  <section>

      <div class="list-left-panel">
        <AddItem
          @info="addItemObj($event)"
          @addClick="addItem()"
        />
        
      </div>

      <div class="list-right-panel">
        <Tiles
        :name="newItem.name"
        :brand="newItem.brand"
        :state="newItem.state"
        :info="newItem.info"
        :cost="newItem.deposit"
        />
        <Tiles 
        :name="item.name" 
        :brand="item.brand" 
        :state="item.state" 
        :info="item.info" 
        :cost="item.cost" 
        :days="item.days_left" 
        v-for="item in items" 
        :key="item.id"
        />
      </div>
  </section>
</template>

<script>
import tiles from './summary/summaryTiles.vue'
import addItem from './summary/summaryAddTiles.vue'
import axios from 'axios';

export default {
  name: 'listItem',
  components: {
    Tiles: tiles,
    AddItem: addItem,
  },
  data: () => {
    return{
      items: [],
      newItem: {name: '', deposit: 0, state: '', info: '', brand: ''}
    }
  },
  methods: {
    addItemObj: function(newItemChild){
      this.newItem = newItemChild;
    },
    addItem: function(){
      axios.post(
      'http://127.0.0.1:5000/deposit_item',
      this.newItem,
      { headers: {'Authorization': "Bearer "+this.$session.get('tokken')}}
      )
      .then(response => (
        console.log(response.data)
        ))
      .catch(error => (
        console.log(error.response)
        ))
      setTimeout(() => {window.location.reload()}, 500)
    }
  },
  beforeMount(){
    if(!this.$session.exists() || this.$session.get('tokken') == "") this.$router.push('/log')

    axios.get(
    'http://127.0.0.1:5000/deposit_items',
    { headers: {'Authorization': "Bearer "+this.$session.get('tokken')}}
    )
    .then(response => (
      console.log(response.data),
      this.items = response.data
      ))
    .catch(error => (
      console.log(error.response),
      this.response = error.response
      ))
  },
}
</script>
 
<style >
  .list-left-panel{
    display: flex;
    position: fixed;
    width:35%;
    height: 84vh;
    background: #663EFF;
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
    background: #18ADD6; 
    width:61%; 
  }
</style>
