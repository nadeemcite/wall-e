import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import {LandingComponent} from './views/landing/landing.component';
import {GeneralService} from './services/general.service';


@NgModule({
  declarations: [
    AppComponent, LandingComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [GeneralService],
  bootstrap: [AppComponent]
})
export class AppModule { }
