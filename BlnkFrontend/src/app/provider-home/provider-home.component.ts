import { Component, OnInit } from '@angular/core';
import { WebService } from '../web.service';

@Component({
  selector: 'app-provider-home',
  templateUrl: './provider-home.component.html',
  styleUrls: ['./provider-home.component.css']
})
export class ProviderHomeComponent {
  newFund: number = 0.0;
  errorMessage: string = "";
  currentUser:any
  loans:any[] = []
  funds:any[] = []
  ngOnInit(): void {
    const sessionUser = sessionStorage.getItem('currentuser')!;
    this.currentUser = JSON.parse(sessionUser);
    this.webService.post(
      'subloan/get_provider_loans/',
      {id:this.currentUser.id}
    ).subscribe((response)=>{
      console.log(response);
      const object:any = response;
      this.loans = object.subloans
    });
    this.fetchProviderFunds();
  }


  constructor(private webService : WebService) {}


  fetchProviderFunds(){
    this.webService.post(
      'fund/get_provider_funds/',
      {provider_id:this.currentUser.id}
    ).subscribe((response:any)=>{
      this.funds = response.provider_funds;
    })
  }

  submitForm(): void {
    // Add logic to submit the new fund to the service
    if(this.newFund > 0){
      console.log(this.currentUser.id)
      this.webService.post(
        'fund/add_fund/',
        {
          provider : this.currentUser.id,
          amount : this.newFund
        }
      ).subscribe((response)=>{
        console.log(response)
        window.location.reload();
      })
    }
    else{
      this.errorMessage = "Fund amount cannot be 0!"
    }

  }

}
