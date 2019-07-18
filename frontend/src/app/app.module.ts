import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { RouterModule, Routes }  from '@angular/router';
import { MatCardModule } from '@angular/material/card';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ListComponent } from './components/list/list.component';
import { ElementsComponent } from './components/elements/elements.component';
import { EffectService } from './services/effectService';
import { ComService } from './services/comService';
import { OctService } from './services/octService';
import { DisService } from './services/disService';

const appRoutes: Routes = [
  { path: 'efekty', component: ElementsComponent },
  { path: 'gitary', component: NavbarComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ListComponent,
    ElementsComponent,
  ],
  imports: [
    BrowserModule,
    NgbModule.forRoot(),
    HttpModule,
    BrowserAnimationsModule,
    MatTabsModule,
    MatIconModule,
    MatButtonToggleModule,
    RouterModule.forRoot(appRoutes),
    MatCardModule,
    
  ],
  providers: [EffectService, ComService, OctService, DisService],
  bootstrap: [AppComponent]
})
export class AppModule { }
