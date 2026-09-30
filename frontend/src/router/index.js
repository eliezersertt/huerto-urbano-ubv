import { createRouter, createWebHistory } from 'vue-router'
import PlantListView from '../views/PlantListView.vue'
import PlantDetailView from '../views/PlantDetailView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'plants',
      component: PlantListView,
    },
    {
      path: '/planta/:censusNumber',
      name: 'plant-detail',
      component: PlantDetailView,
      props: true,
    },
  ],
})

export default router
