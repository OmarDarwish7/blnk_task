import { Component } from '@angular/core';
import { WebService } from '../web.service';
import { HttpResponse } from '@angular/common/http';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username = ""
  password = ""

  constructor(
    private webService : WebService,
    private router : Router
  ){}

  ngOnInit(): void {
  }

  onSubmit() {
    if(this.username != ""  && this.password != "")
    this.webService.post(
      'users/login/',
      {
        username:this.username,
        password:this.password
      }
      ).subscribe((response)=>{
        const object:any = response
        console.log(object)
        if(object.data){
            sessionStorage.setItem('currentuser',JSON.stringify(object.data))
            if(object.data.user_type == 'loan_provider'){
              this.router.navigate(['provider_home'])
            }
            else if(object.data.user_type == 'loan_customer'){
              this.router.navigate(['customer_home'])
            }
            else if(object.data.user_type == 'bank_personnel'){
              this.router.navigate(['personnel_home'])
            }
        }
      });
  }
}
