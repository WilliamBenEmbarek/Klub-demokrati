import React from 'react';
import './NowPlaying.css'

class NowPlaying extends React.Component {
    render() {
        return(
                // eslint-disable-next-line
                <div className="SongCover"><img className='NowPlayingArt' src={this.props.image}/>
                    <div className='songText'>{this.props.songName} - {this.props.artist}: Votes {this.props.votes}</div>
                </div>
                // TODO Timer?
        );
    }
}
export default NowPlaying;