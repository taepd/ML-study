import React from 'react'
import {UserMenu as Menu} from '../components'
import './table.style.css'

const User = ({children}) => (<>
    <h1>User</h1>
    <Menu/>
    {children}
</>)

export default User


