

<template>
<h1 class="text-white ">
  penis
</h1>
</template>

<style scoped>

</style>

<script setup>
import {onMounted} from 'vue'
import axios from 'axios'

onMounted(() =>{
  getProfile()
})

function getProfile(){
  console.log('getting profile')

  // axios
  //         .post('/api/search', {
  //           query: this.summonerName
  //         })
  //         .then(response=>{
  //           console.log('response:', response.data)
  //
  //           if(response.data.message ==='exists'){
  //             // if user exists, pushes them to profile view with their name
  //
  //             this.$router.push(`/profile/${response.data.name}`)
  //           }
  //
  //           if(response.data.message ==='does not exist'){
  //             //TODO have a toast or something saying that the user doesnt exist
  //           }
  //         })
  //         .catch(error =>{
  //           console.log('error', error)
  //         })
}

</script>