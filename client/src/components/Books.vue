<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>SPUs</h1>
        <hr><br><br>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-prefix-group"
                      label="Prefix:"
                      label-for="form-prefix-input">
            <b-form-input id="form-prefix-input"
                          type="text"
                          v-model="addSPUForm.prefix"
                          required
                          placeholder="CD">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-date-group"
                        label="Date:"
                        label-for="form-date-input">
            <b-form-input id="form-date-input"
                          type="text"
                          v-model="addSPUForm.date"
                          required
                          placeholder="date">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-category-group"
                        label="Category:"
                        label-for="form-category-input">
            <b-form-input id="form-date-input"
                          type="text"
                          v-model="addSPUForm.category"
                          required
                          placeholder="Category">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-seq-group"
                        label="Sequence:"
                        label-for="form-sequence-input">
            <b-form-input id="form-seq-input"
                          type="text"
                          v-model="addSPUForm.seq"
                          required
                          placeholder="seq">
            </b-form-input>
          </b-form-group>
          <b-alert show>{{ spu }}</b-alert>
         <!--  <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
              <b-form-checkbox value="true">Read?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group> -->
          <b-button type="submit" variant="primary">Generate</b-button>
        </b-form>
        <br><br>
        Total SPU Genrated: {{spu_count}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Books',
  data() {
    return {
      spu_count: 0,
      addSPUForm: {
        prefix: '',
        date: '',
        category: '',
        seq: 0,
      },
      spu: '',
    };
  },
  methods: {
    getSPUCount() {
      const path = 'http://localhost:5000/spu_count';
      axios.get(path)
        .then((res) => {
          this.spu_count = res.data.spu_count;
          this.addSPUForm.seq = this.spu_count + 1;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addSPU(payload) {
      const path = 'http://localhost:5000/spu_count';
      axios.post(path, payload)
        .then((response) => {
          console.log(response);
          this.spu = response.data.spu;
          this.getSPUCount();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSPUCount();
        });
    },
    initForm() {
      this.addSPUForm.prefix = 'CD';
      this.addSPUForm.date = this.$moment(new Date()).format('YYYYMMDD');
      this.addSPUForm.seq = this.spu_count + 1;
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        prefix: this.addSPUForm.prefix,
        seq: this.addSPUForm.seq,
        date: this.addSPUForm.date,
        category: this.addSPUForm.category,
      };
      this.addSPU(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
  created() {
    this.getSPUCount();
    this.initForm();
  },
};
</script>
