import React from 'react'  // 전역은 package.js에서 찾는다
import {About, Contact, Events, Home, Products, Error} from '../components'
import {BrowserRouter, Route, Switch, Redirect} from 'react-router-dom'

const Main = () => <>
        <BrowserRouter>
            <div className="main">
                <Switch>
                    <Route exact path="/" component={Home}/>
                    <Route path="/about" component={About}/>
                    <Redirect from={"/history"} to={"/about/history"}/>
                    <Redirect from={"/services"} to={"/about/serviced"}/>
                    <Redirect from={"/location"} to={"/about/location"}/>
                    <Route path="/contact" component={Contact}/>
                    <Route path="/events" component={Events}/>
                    <Route path="/products" component={Products}/>
                    <Route component={Error}/>   {/* 경로가 없으면 Error로 보냄*/}
                </Switch>
            </div>

        </BrowserRouter>
    </>

export default Main
