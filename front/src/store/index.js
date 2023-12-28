import Vuex from 'vuex';
import typeFace from "@/store/modules/typeFace"; // Импортируйте Vue
import Signup from "@/store/modules/Signup";
import ProfileModule from "@/store/modules/ProfileModule"
import GetData from "@/store/modules/GetData"
import FetchUserResults from "@/store/modules/FetchUserResults";
import FetchMedicines from "@/store/modules/FetchMedicines";
import FetchProduct from "@/store/modules/FetchProduct";
import Cart from "@/store/modules/Cart";
import User from "@/store/modules/User";
export default  new Vuex.Store({
    modules:{Signup,ProfileModule,GetData,FetchUserResults,FetchMedicines,FetchProduct,Cart, User}
});
