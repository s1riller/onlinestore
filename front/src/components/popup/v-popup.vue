<script>
export default {
  name: "v-popup",
  props: {
    popupName: String,
    popupSize: Object,
    firstName: String,
    lastName: String,
  },
  data() {
    return {}

  },

  computed: {},
  methods:{
    closePopup(){
      this.$emit('closePopup')
    },
  }
}

</script>

<template>
  <div class="v-popup" :style="{ width: popupSize.width, height: popupSize.height }">
    <div class="v-popup__header">
      <span> {{popupName}}</span>
      <span>
        <button class="btn"><i class="material-icons"
           @click="closePopup"
        >close</i>
          </button>
      </span>
    </div>
    <div class="v-popup__content">
      <slot></slot>
    </div>
    <div class="v-popup__footer">
      <button class="btn" @click="closePopup">OK</button>
    </div>
  </div>
</template>

<style>
.v-popup {
  padding: 16px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  background: #ffffff;
  box-shadow: 0 0 17px 0 #e7e7e7;
  z-index:10;

}


.v-popup__header,
.v-popup__footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.v-popup__content {
  display: flex;
  justify-content: center;
  align-items: center;
}




</style>