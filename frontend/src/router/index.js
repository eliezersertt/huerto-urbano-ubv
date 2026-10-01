import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PlantListView from '../views/PlantListView.vue'
import PlantDetailView from '../views/PlantDetailView.vue'
import InventoryView from '../views/InventoryView.vue'
import CyclesView from '../views/CyclesView.vue'
import SeedbedsView from '../views/SeedbedsView.vue'
import PeopleView from '../views/PeopleView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/censo',
      name: 'plants',
      component: PlantListView,
    },
    {
      path: '/planta/:censusNumber',
      name: 'plant-detail',
      component: PlantDetailView,
      props: true,
    },
    {
      path: '/inventario',
      name: 'inventory',
      component: InventoryView,
    },
    {
      path: '/ciclos',
      name: 'cycles',
      component: CyclesView,
    },
    {
      path: '/semilleros',
      name: 'seedbeds',
      component: SeedbedsView,
    },
    {
      path: '/responsables',
      name: 'people',
      component: PeopleView,
    },
  ],
})

export default router
