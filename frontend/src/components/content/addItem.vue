<template>
  <section>

      <div class="list-left-panel">
        <AddItem
          @info="addItemObj($event)"
        />
      </div>

      <div class="list-right-panel">
        <Tiles
        :name="newItem.name"
        :brand="newItem.brand"
        :state="newItem.state"
        :info="newItem.info"
        :cost="newItem.cost"
        :newCost="newItem.newCost"
        />
        <Tiles 
        :name="item.name" 
        :brand="item.brand" 
        :state="item.state" 
        :info="item.info" 
        :cost="item.cost" 
        :newCost="item.newCost" 
        :id="item.id"
        v-for="item in items" 
        :key="item.id"
        />
      </div>

  </section>
</template>

<script>
import tiles from './listItem/tiles.vue'
import addItem from './addItem/addTiles.vue'

export default {
  name: 'listItem',
  components: {
    Tiles: tiles,
    AddItem: addItem,
  },
  props: ['logged'],
  data: () => {
    return{
      items: [
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 1},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 2},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 3},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 4},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 5},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 6},
        {name: 'name', cost: 'cost', state: 'state', info: 'info', brand: 'brand', newCost: 'newCost', id: 7},
      ],
      newItem: {name: '', cost: 0, state: '', info: '', brand: '', newCost: 0, id: null}
    }
  },
  methods: {
    addItemObj: function(newItemChild){
      this.newItem = newItemChild;
      // console.log(this.newItem.name+" "+newItemChild.name);
    }
  },
  beforeMount(){
    if(this.logged == false) this.$router.push('/log')
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
