import {createRouter, createWebHistory} from "vue-router";

import Home from "@/pages/Home"
import Testing from "@/views/Test.vue"
import Performance from "@/pages/PerformancePage.vue"
import Statistics from "@/pages/ StatisticsPage.vue";
import Products from "@/pages/ProductsPage.vue";
import Shop from "@/views/Shop.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Account from "@/views/Account.vue";
import Profile from "@/views/Profile.vue"
import AddProduct from "@/views/AddProduct.vue";
import UploadImage from "@/views/UploadImage.vue";
import Cart from "@/views/Cart.vue";
import Reports from "@/views/Reports.vue";
import VolumeOfSales from "@/views/report/VolumeOfSales.vue";
import FinancialReport from "@/views/report/FinancialReport.vue"
import SalesByCategory from "@/views/report/SalesByCategory.vue";
import AverageOrderValuePerUser from "@/views/report/AverageOrderValuePerUser.vue"
import UserTestResultsReport from "@/views/report/UserTestResultsReport.vue"
import UsersList from "@/views/report/UsersList.vue";
import ListSoldProducts from "@/views/report/ListSoldProducts.vue";
const routes = [
    {path: "/", component: Home, name: 'Home'},
    {path: "/Test", component: Testing, name: 'Test'},
    {path: "/Shop", component: Shop, name: 'Shop'},
    {path: "/Statistic", component: Statistics},
    {path: '/Performance', component: Performance, name: 'performance'},
    {path: '/Products', component: Products, name: 'products'},
    {path: '/Login', component: Login, name: 'Login'},
    {path: '/Register', component: Register, name: 'Register'},
    {path: '/Account', component: Account, name: 'Account'},
    {path: '/Profile', component: Profile, name: 'Profile'},
    {path: '/AddProduct', component: AddProduct, name: 'AddProduct'},
    {path: '/UploadImage', component: UploadImage, name: 'UploadImage'},
    {path: '/Cart', component: Cart, name: 'Cart'},
    {path: '/Reports', component: Reports, name: 'Reports'},
    {path: '/VolumeOfSales', component: VolumeOfSales, name: 'VolumeOfSales'},
    {path: '/FinancialReport', component: FinancialReport, name: 'FinancialReport'},
    {path: '/SalesByCategory', component: SalesByCategory, name: 'SalesByCategory'},
    {path: '/AverageOrderValuePerUser', component: AverageOrderValuePerUser, name: 'AverageOrderValuePerUser'},
    {path: '/UserTestResultsReport', component: UserTestResultsReport, name: 'UserTestResultsReport'},
    {path: '/UsersList', component: UsersList, name: 'UsersList'},
    {path: '/ListSoldProduct', component: ListSoldProducts, name: 'ListSoldProduct'}

];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});


// router.beforeEach((to, from, next) => {
//   if (to.path !== '/' && localStorage.getItem('token') === 'null') {
//
//
//
//       Home.methods.openModal()
//
//
//
//     next('/');
//   } else {
//     next();
//   }
// });

export default router;
