import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ProviderHomeComponent } from './provider-home/provider-home.component';
import { CustomerHomeComponent } from './customer-home/customer-home.component';
import { PersonnelHomeComponent } from './personnel-home/personnel-home.component';

const routes: Routes = [
  {path:'',component:LoginComponent},
  {path:'provider_home',component:ProviderHomeComponent},
  {path:'customer_home',component:CustomerHomeComponent},
  {path:'personnel_home',component:PersonnelHomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
