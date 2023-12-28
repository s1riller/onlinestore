<!-- StarRating.vue -->
<template>
  <div class="star-rating">
    <i
        v-for="star in 5"
        :key="star"
        class="star"
        :class="{ 'filled': star <= rating }"
        @click="selectRating(star)"
    ></i>
  </div>
</template>

<script>
export default {
  props: {
    initialRating: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      rating: this.initialRating,
    };
  },
  methods: {
    selectRating(star) {
      this.rating = star;
      // You can emit an event to send the rating to the parent component
      this.$emit('rating-selected', this.rating);
    },
  },
};
</script>

<style scoped>
/* Add your star rating CSS styles here */
</style>
