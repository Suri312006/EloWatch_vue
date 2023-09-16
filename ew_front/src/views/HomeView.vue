

<template>
  <div class="bg-black scroll-smooth">
    <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&display=swap" rel="stylesheet">
    
    <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&family=PT+Mono&display=swap" rel="stylesheet">

    <div class="flex justify-center items-center h-screen">
      <div class="bg-black rounded-sm p-4 shadow-md">
        <input
          type="text"
          class="w-64 py-2 px-4 border rounded-sm font-nova-pt-mono "
          placeholder="Summoner name" 
          v-model="summonerName"
          @keydown.enter="search"
        />
        <button
          class="ml-2 px-4 py-2 bg-white font-nova-mono text-black rounded-sm hover:bg-gray-400"
          @click="search"
        >
          Search
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Add any additional styling you want for your search bar here */
/* Add any additional styling you want for your toolbar here */
.font-nova-mono {
  font-family: 'Nova Mono', monospace;
  /* You can adjust the font size, letter spacing, and other properties here */
  letter-spacing: 0px;
  text-shadow: 2px 2px 3px rgba(255, 255, 255, 0.5);
}
.font-nova-pt-mono{
  
font-family: 'PT Mono', monospace;

}

</style>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      summonerName: '',
    };
  },
  created() {
    setTimeout(()=>{
      this.delayedScrollToBottom();
    }, 700)
    
  },
  methods: {
    search() {
      // Implement your search logic here
      console.log('Searching for:', this.summonerName);
      axios
          .post('/query/', {
            query: this.summonerName
          })
          .then(response=>{
            console.log('response:', response.data)

            if(response.data.message ==='exists'){
              // if user exists, pushes them to profile view with their name

              this.$router.push(`/profile/${response.data.name}`)
            }

            if(response.data.message ==='does not exist'){
              //TODO have a toast or something saying that the user doesnt exist
            }
          })
          .catch(error =>{
            console.log('error', error)
          })
      // this.summonerName = ''
    },





    delayedScrollToBottom() {
      const duration = 1000; // Animation duration in milliseconds
      const start = performance.now();

      function animateScroll(timestamp) {
        const elapsed = timestamp - start;

        if (elapsed < duration) {
          const easingFactor = Math.pow(elapsed / duration, 7); // You can adjust the power for different acceleration curves
          const scrollPosition = easingFactor * (document.documentElement.scrollHeight - window.innerHeight);
          window.scrollTo(0, scrollPosition);

          requestAnimationFrame(animateScroll);
        } else {
          window.scrollTo(0, document.documentElement.scrollHeight);
        }
      }

      requestAnimationFrame(animateScroll)
    },

  },
};
</script>

