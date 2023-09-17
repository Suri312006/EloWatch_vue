<script>
export default {
  name: "Rank",
  props: {
    rank_data: Object,
    required: true,
  }
}
</script>

<template>
<h1 class="text-blue-700">
  {{ rank_data }}
</h1>
</template>

<style scoped>

</style>