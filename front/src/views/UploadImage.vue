<template>
  <div class="container">
    <div class="row">
      <div class="col-sm ">
        <div class="row text-center">
          <div class="col-12"><input id="img" class="form-control" type="file" @change="handleFileChange"/></div>
          <div class="row text-center" v-if="imageSrc">
            <div class="col-3"><h4>ширина</h4><input v-model="widthImage" class="form-control" disabled type="text"/>
            </div>
            <div class="col-3"><h4>высота</h4><input v-model="heightImage" class="form-control" disabled type="text"/>
            </div>
            <div class="col-3"><h4>тип</h4><input v-model="typeImage" class="form-control" disabled type="text"/></div>
            <div class="col-3"><h4>размер</h4><input v-model="weightImage" class="form-control" disabled type="text"/>
            </div>
            <div class="col-12"><h4>название</h4><input v-model="nameImage" class="form-control" disabled type="text"/>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm">
        <img v-if="imageSrc" :src="imageSrc" alt="Загруженное изображение" class="img-fluid rounded-5">

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'v-upload-image',
  data() {
    return {
      widthImage: null,
      heightImage: null,
      typeImage: null,
      weightImage: null,
      nameImage: null,
      imageSrc: null,
      showInfo: false,
    }
  },
  methods: {
    handleFileChange(e) {
      const file = e.target.files[0];
      if (file) {
        this.nameImage = file.name.substring(0, file.name.indexOf('.'));
        this.typeImage = file.type.substring(file.type.indexOf('/') + 1);
        this.weightImage = `${(file.size / 1000000).toFixed(2)}MB`

        let _this = this
        const reader = new FileReader()
        reader.onload = function (event) {
          let image = new Image();
          image.onload = function () {
            _this.widthImage = `${image.width}px`
            _this.heightImage = `${image.height}px`
            _this.imageSrc = event.target.result
          };
          image.src = event.target.result;
        };
        reader.readAsDataURL(file);
      }
    }
  }
}
</script>

<style scoped>
/* Ваши стили здесь */
</style>
