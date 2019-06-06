import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes }  from '@angular/router';
import { ListComponent } from './../components/list/list.component';
import { NavbarComponent } from './../components/navbar/navbar.component';
import { ElementsComponent } from './../components/elements/elements.component';



const routes: Routes = [

  { path: 'home', component: ListComponent },
  { path: 'nav', component: NavbarComponent },
  { path: 'ele', component: ElementsComponent },

  
];



@NgModule({

  imports: [CommonModule, RouterModule.forRoot(routes)],
  declarations: [RouterModule]
})
export class AppRoutingModule { }
